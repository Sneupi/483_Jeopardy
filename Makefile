.PHONY: all install clean run test rerank hybrid-tfidf

SHELL := /bin/bash
PYTHON_VENV := .venv/bin/python

# NOTE:
# 	Alternatively, could run 
#   `source ./.venv/bin/activate`
# 	and run Python programs manually

all: clean install test

install:
	./install.sh

clean: 
	rm -rf .bm25s
	rm -rf .tfidf
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf utils/__pycache__

run: $(PYTHON_VENV)
	$(PYTHON_VENV) utils/retriever.py .bm25s

rerank: $(PYTHON_VENV)
	$(PYTHON_VENV) utils/reranker.py .bm25s

hybrid-tfidf: $(PYTHON_VENV)
	$(PYTHON_VENV) utils/retriever_hybrid.py .bm25s

test: $(PYTHON_VENV)
	$(PYTHON_VENV) -m pytest

test-bm25:
	$(PYTHON_VENV) -m pytest tests/test_questions.py -v --tb=short

test-reranker:
	$(PYTHON_VENV) -m pytest tests/test_reranker_questions.py -v --tb=short

test-hybrid-tfidf:
	$(PYTHON_VENV) -m pytest tests/test_bm25tfidf_questions.py -v --tb=short

compare:
	@echo "=== BM25 Baseline ===" && $(PYTHON_VENV) -m pytest tests/test_questions.py::test_topK -q --tb=no || true
	@echo "\n=== Semantic Reranker (embeddings top-100) ===" && $(PYTHON_VENV) -m pytest tests/test_reranker_questions.py::test_topK_reranker -q --tb=no || true
	@echo "\n=== BM25 + TF-IDF ===" && $(PYTHON_VENV) -m pytest tests/test_bm25tfidf_questions.py::test_topK_bm25tfidf -q --tb=no || true