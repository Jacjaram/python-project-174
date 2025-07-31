lint:
	poetry run flake8

install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml

check:
	poetry run flake8 gendiff
	poetry run pytest
	
run-diff:
	python -m gendiff.scripts.gendiff tests/fixtures/file1.json tests/fixtures/file2.json
