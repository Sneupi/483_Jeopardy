.PHONY: clean run test

SHELL := /bin/bash

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf wiki
	rm -rf .venv

run: 
	python3 mini_watson.py wiki

test: 
	pytest