.PHONY: clean run test dev

SHELL := /bin/bash
PYTHON_VENV := .venv/bin/python

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf wiki
	rm -rf .venv

run: $(PYTHON_VENV)
	$(PYTHON_VENV) mini_watson.py wiki index

test: $(PYTHON_VENV)
	 $(PYTHON_VENV) -m pytest

# small test collection
dev:
	clear
	rm -rf dev/index
	$(PYTHON_VENV) mini_watson.py dev/wiki dev/index
