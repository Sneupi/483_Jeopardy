.PHONY: run test

SHELL := /bin/bash
PYTHON_VENV := .venv/bin/python

# NOTE:
# 	Alternatively, could run 
#   `source ./.venv/bin/activate`
# 	and run Python programs manually

run: $(PYTHON_VENV)
	$(PYTHON_VENV) utils/retriever.py .bm25s

test: $(PYTHON_VENV)
	$(PYTHON_VENV) tests/meta_test_questions.py tests/questions.txt .bm25s tests
	$(PYTHON_VENV) -m pytest