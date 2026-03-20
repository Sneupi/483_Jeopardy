.PHONY: clean venv run test

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf wiki
	rm -rf .venv

venv:
	source .venv/bin/activate

run: venv
	python3 mini_watson.py wiki

test: venv
	pytest