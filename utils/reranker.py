# Semantic reranker for BM25s results
# Reranks top-k BM25s results using embedding-based semantic similarity

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from utils.retriever import Retriever

try:
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False


class SemanticReranker:
    """
    Reranks BM25s results using embedding-based semantic similarity.
    - Gets top-k from BM25s
    - Embeds top-k results + query
    - Reranks by semantic similarity
    
    Advantage: Only embeds k results per query (not all 280k docs)
    """
    
    def __init__(self, bm25_index_dir, model_name="all-MiniLM-L6-v2"):
        """
        Initialize reranker with BM25s retriever and embedding model.
        
        Args:
            bm25_index_dir: Path to BM25s index
            model_name: Sentence transformer model to use
        """
        self.retriever = Retriever(bm25_index_dir)
        self.model = SentenceTransformer(model_name)
    
    def rerank(self, query, k=100, rerank_k=None):
        """
        Rerank top-k BM25s results using semantic similarity.
        
        Args:
            query: Question/query string
            k: Number of initial BM25s results to rerank
            rerank_k: If specified, only rerank top rerank_k (for speed)
        
        Returns:
            results: Reranked document results
            scores: Reranked similarity scores
        """
        
        # Get initial BM25s results
        bm25_results, bm25_scores = self.retriever.run_query(query, k=k)
        
        # Decide how many to rerank
        if rerank_k is None:
            rerank_k = min(k, bm25_results.shape[1])
        else:
            rerank_k = min(rerank_k, bm25_results.shape[1])
        
        # Extract documents to rerank
        docs_to_rerank = []
        for i in range(rerank_k):
            doc = bm25_results[0, i]
            # Combine title and text for better semantic representation
            text = f"{doc['title']} {doc['text']}"
            docs_to_rerank.append(text)
        
        # Embed query and documents
        query_embedding = self.model.encode(query, convert_to_numpy=True)
        doc_embeddings = self.model.encode(docs_to_rerank, convert_to_numpy=True)
        
        # Compute semantic similarity
        similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
        
        # Sort by similarity
        sorted_indices = np.argsort(-similarities)
        
        # Reorder results
        reranked_results = []
        reranked_scores = []
        
        for idx in sorted_indices:
            doc = bm25_results[0, idx]
            reranked_results.append(doc)
            reranked_scores.append(similarities[idx])
        
        # Add remaining results (beyond rerank_k) in original BM25s order
        for i in range(rerank_k, bm25_results.shape[1]):
            doc = bm25_results[0, i]
            reranked_results.append(doc)
            # Use normalized BM25s score for these
            reranked_scores.append(max(0, float(bm25_scores[0, i]) / 100))
        
        # Convert to numpy arrays in expected format
        results_array = np.array([reranked_results])
        scores_array = np.array([reranked_scores])
        
        return results_array, scores_array


def main(bm25_index_dir):
    """Interactive query loop with semantic reranking."""
    
    reranker = SemanticReranker(bm25_index_dir)
    
    while True:
        query = input('\nQuery: ').strip()
        if query.lower() == 'exit':
            break
        
        results, scores = reranker.rerank(query, k=100, rerank_k=50)
        
        print(f"\n{'Rank':<4} {'Score':<8} {'Title'}")
        print("-" * 70)
        
        for i in range(min(10, results.shape[1])):
            doc = results[0, i]
            score = scores[0, i]
            print(f"{i+1:<4} {score:>6.3f}  {doc['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <bm25_index_dir>")
        exit(-1)
    
    main(sys.argv[1])
