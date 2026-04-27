.PHONY: all install clean run test

SHELL := /bin/bash
PYTHON_VENV := .venv/bin/python

# NOTE:
# 	Alternatively, could run 
#   `source ./.venv/bin/activate`
# 	and run Python programs manually

all: clean install test eval

install:
	./install.sh

clean: 
	rm -rf .venv
	rm -rf .wiki
	rm -rf .index.bm25s

run: $(PYTHON_VENV)
	$(PYTHON_VENV) retrievers.py

test: $(PYTHON_VENV)
	-$(PYTHON_VENV) -m pytest

eval: $(PYTHON_VENV)
	$(PYTHON_VENV) eval.py