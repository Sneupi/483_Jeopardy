# BM25 + TF-IDF hybrid retriever
# Fast dual search on full 280k corpus

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.retriever import Retriever


class BM25TfidfRetriever:
    """
    Dual hybrid: BM25 + TF-IDF (no embeddings)
    - Fast: both methods use standard text indexing
    - Effective: different relevance weighting helps
    """
    
    def __init__(self, bm25_index_dir, tfidf_index_dir=".tfidf"):
        """
        Initialize retriever with BM25 and TF-IDF.
        
        Args:
            bm25_index_dir: Path to BM25s index
            tfidf_index_dir: Path to TF-IDF index
        """
        import pickle
        from scipy.sparse import load_npz
        
        self.retriever = Retriever(bm25_index_dir)
        
        # Load pre-built TF-IDF index
        if not os.path.exists(tfidf_index_dir):
            raise FileNotFoundError(
                f"TF-IDF index not found at {tfidf_index_dir}. "
                f"Run: python utils/tfidf_indexer.py {tfidf_index_dir} .wiki"
            )
        
        print(f"Loading TF-IDF index from {tfidf_index_dir}...")
        
        vectorizer_path = os.path.join(tfidf_index_dir, "vectorizer.pkl")
        matrix_path = os.path.join(tfidf_index_dir, "matrix.npz")
        
        with open(vectorizer_path, 'rb') as f:
            self.tfidf_vectorizer = pickle.load(f)
        
        self.tfidf_matrix = load_npz(matrix_path)
        
        print(f"Loaded TF-IDF matrix: {self.tfidf_matrix.shape}")
    
    def run_query(self, query, k=100):
        """
        Hybrid search: BM25 + TF-IDF with RRF merging.
        
        Args:
            query: Query string
            k: Number of results to return
        
        Returns:
            results: Merged document results
            scores: Merged scores
        """
        
        # 1. BM25 search
        bm25_results, bm25_scores = self.retriever.run_query(query, k=k*2)
        
        # 2. TF-IDF search
        query_tfidf = self.tfidf_vectorizer.transform([query])
        tfidf_scores = cosine_similarity(query_tfidf, self.tfidf_matrix)[0]
        top_tfidf_indices = np.argsort(-tfidf_scores)[:k*2]
        
        # Merge using RRF
        rank_dict = {}
        
        # Add BM25 results
        for rank, (doc, score) in enumerate(zip(bm25_results[0], bm25_scores[0])):
            doc_id = doc["id"]
            rrf_score = 1.0 / (60 + rank)
            rank_dict[doc_id] = {
                "doc": doc,
                "bm25_rrf": rrf_score,
                "tfidf_rrf": 0.0
            }
        
        # Add TF-IDF results
        for rank, idx in enumerate(top_tfidf_indices):
            doc = self.retriever.retriever.corpus[idx]
            doc_id = doc["id"]
            rrf_score = 1.0 / (60 + rank)
            
            if doc_id in rank_dict:
                rank_dict[doc_id]["tfidf_rrf"] = rrf_score
            else:
                rank_dict[doc_id] = {
                    "doc": doc,
                    "bm25_rrf": 0.0,
                    "tfidf_rrf": rrf_score
                }
        
        # Combine scores
        for doc_id in rank_dict:
            entry = rank_dict[doc_id]
            combined = (entry["bm25_rrf"] + entry["tfidf_rrf"]) / 2
            entry["combined_score"] = combined
        
        # Sort and return top-k
        sorted_results = sorted(
            rank_dict.items(),
            key=lambda x: x[1]["combined_score"],
            reverse=True
        )[:k]
        
        results = np.array([[item[1]["doc"] for item in sorted_results]])
        scores = np.array([[item[1]["combined_score"] for item in sorted_results]])
        
        return results, scores


def main(bm25_index_dir, tfidf_index_dir=".tfidf"):
    """Interactive query loop."""
    ir = BM25TfidfRetriever(bm25_index_dir, tfidf_index_dir)
    
    while True:
        query = input('\nQuery: ').strip()
        if query.lower() == 'exit':
            break
        
        results, scores = ir.run_query(query, k=10)
        
        print(f"\n{'Rank':<4} {'Score':<8} {'Title'}")
        print("-" * 70)
        
        for i in range(results.shape[1]):
            doc = results[0, i]
            score = scores[0, i]
            print(f"{i+1:<4} {score:>6.4f}  {doc['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <bm25_index_dir> [tfidf_index_dir]")
        exit(-1)
    
    bm25_dir = sys.argv[1]
    tfidf_dir = sys.argv[2] if len(sys.argv) > 2 else ".tfidf"
    
    main(bm25_dir, tfidf_dir)
