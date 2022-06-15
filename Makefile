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
	pipenv run mypy src

.PHONY: format-check
format-check:
	pipenv run black --config pyproject.toml --diff --check ./
	pipenv run isort --settings-path pyproject.toml --check-only **/*.py

.PHONY: format
format:
	pipenv run isort --settings-path pyproject.toml **/*.py
	pipenv run black --config pyproject.toml ./

.PHONY: test
test:
	pipenv run pytest tests

.PHONY: lint
lint:
	PYTHONPATH=./src pylint ./src

start:
	PYTHONPATH=./src uvicorn  main:app --reload

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
