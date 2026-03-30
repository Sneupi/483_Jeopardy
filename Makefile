.PHONY: clean run test

SHELL := /bin/bash
PYTHON_VENV := .venv/bin/python

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf wiki
	rm -rf .venv

run: $(PYTHON_VENV)
	$(PYTHON_VENV) mini_watson.py wiki

test: $(PYTHON_VENV)
	 $(PYTHON_VENV) -m pytest