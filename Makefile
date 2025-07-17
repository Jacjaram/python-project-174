lint:
	poetry run flake8

install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml

check:
	poetry run flake8 gendiff
	poetry run pytest