# TF-IDF indexer - builds and caches TF-IDF index
# Similar to utils/indexer.py for BM25s

import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from parser import yield_docs


def create_tfidf_index(index_dir, dataset_dir):
    """
    Create and save TF-IDF index.
    
    Args:
        index_dir: Directory to save TF-IDF index
        dataset_dir: Directory containing wiki documents
    """
    
    os.makedirs(index_dir, exist_ok=True)
    
    # Load all documents
    print("Reading documents...")
    corpus_texts = []
    
    for i, (path, title, body) in enumerate(yield_docs(dataset_dir)):
        if i % 50000 == 0:
            print(f"  Loaded {i} documents...")
        text = f"{title} {body}"
        corpus_texts.append(text)
    
    print(f"Total documents: {len(corpus_texts)}")
    
    # Build TF-IDF
    print("Building TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer(
        max_features=10000,
        lowercase=True,
        stop_words='english',
        ngram_range=(1, 2),
        max_df=0.8,
        min_df=2
    )
    
    tfidf_matrix = vectorizer.fit_transform(corpus_texts)
    print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")
    
    # Save
    vectorizer_path = os.path.join(index_dir, "vectorizer.pkl")
    matrix_path = os.path.join(index_dir, "matrix.npz")
    
    print(f"Saving vectorizer to {vectorizer_path}...")
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print(f"Saving matrix to {matrix_path}...")
    from scipy.sparse import save_npz
    save_npz(matrix_path, tfidf_matrix)
    
    print("Done!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <index_dir> <dataset_dir>")
        exit(-1)
    
    create_tfidf_index(index_dir=sys.argv[1], dataset_dir=sys.argv[2])
