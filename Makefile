.PHONY: all install clean run test

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
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf utils/__pycache__

run: $(PYTHON_VENV)
	$(PYTHON_VENV) utils/retriever.py .bm25s

test: $(PYTHON_VENV)
	$(PYTHON_VENV) -m pytest