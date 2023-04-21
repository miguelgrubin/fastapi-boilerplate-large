.PHONY: install-pyenv
install-pyenv:
	curl https://pyenv.run | bash

.PHONY: install-pipenv
install-pipenv:
	pip install --user pipenv

.PHONY: install
install:
	pipenv install --dev

.PHONY: audit
audit:
	pipenv check

.PHONY: typecheck
typecheck:
	mypy src

.PHONY: format-check
format-check:
	black --config pyproject.toml --diff --check ./
	isort --settings-path pyproject.toml --check-only **/*.py

.PHONY: format
format:
	isort --settings-path pyproject.toml .
	black --config pyproject.toml ./

.PHONY: test
test:
	pytest tests

.PHONY: coverage
coverage:
	coverage run -m pytest
	coverage report
	coverage html

.PHONY: lint
lint:
	PYTHONPATH=./src pylint ./src

.PHONY: start
start:
	PYTHONPATH=./src uvicorn  main:app --reload

.PHONY: clean
clean: clean-pyc clean-test clean-docs clean-build

## Remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -not -path "./venv/*" -exec rm -f {} +
	find . -name '*.pyo' -not -path "./venv/*" -exec rm -f {} +
	find . -name '*~' -not -path "./venv/*" -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

## Remove docs static site
clean-docs:
	rm -fr site/

## Remove test and coverage artifacts
clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -f coverage.xml
	rm -f pytest.xml
	rm -f pylint-report.txt
	rm -fr htmlcov/
	rm -fr .pytest_cache

## Remove build artifacts
clean-build:
	rm -fr build
	rm -fr *.egg-info

.PHONY: migration-generate
migration-generate:
	@echo "To be implemented"

.PHONY: migration-run
migration-run:
	@echo "To be implemented"

.PHONY: migration-revert
migration-revert:
	@echo "To be implemented"

.PHONY: seed
seed:
	@echo "To be implemented"
