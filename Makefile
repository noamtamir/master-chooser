venv:
	python -m venv .venv

install:
	poetry install --no-root

run:
	poetry run choose-master

test:
	poetry run python -m unittest