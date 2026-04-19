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
    
    def __init__(self, bm25_index_dir):
        """
        Initialize retriever with BM25 and TF-IDF.
        
        Args:
            bm25_index_dir: Path to BM25s index
        """
        self.retriever = Retriever(bm25_index_dir)
        
        # Check if TF-IDF is cached
        import pickle
        tfidf_cache = ".tfidf_cache.pkl"
        
        if os.path.exists(tfidf_cache):
            print("Loading cached TF-IDF index...")
            with open(tfidf_cache, 'rb') as f:
                self.tfidf_vectorizer, self.tfidf_matrix = pickle.load(f)
            print(f"Loaded TF-IDF matrix: {self.tfidf_matrix.shape}")
        else:
            # Build TF-IDF index (only first time)
            print("Building TF-IDF index on 280k documents (this takes ~5 minutes on first run)...")
            corpus_texts = []
            for i, doc in enumerate(self.retriever.retriever.corpus):
                if i % 50000 == 0:
                    print(f"  Processing document {i}...")
                text = f"{doc['title']} {doc['text']}"
                corpus_texts.append(text)
            
            self.tfidf_vectorizer = TfidfVectorizer(
                max_features=10000,
                lowercase=True,
                stop_words='english',
                ngram_range=(1, 2),
                max_df=0.8,
                min_df=2
            )
            self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(corpus_texts)
            print(f"TF-IDF matrix built: {self.tfidf_matrix.shape}")
            
            # Cache for next time
            print("Caching TF-IDF index for future runs...")
            with open(tfidf_cache, 'wb') as f:
                pickle.dump((self.tfidf_vectorizer, self.tfidf_matrix), f)
            print("Cached!")
    
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


def main(bm25_index_dir):
    """Interactive query loop."""
    ir = BM25TfidfRetriever(bm25_index_dir)
    
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
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <bm25_index_dir>")
        exit(-1)
    
    main(sys.argv[1])
