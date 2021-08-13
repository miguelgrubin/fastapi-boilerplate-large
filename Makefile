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
	pipenv run mypy --config-file setup.cfg src/**/*.py tests/**/*.py

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
	pipenv run pytest --ignore=tests/with_real_server

.PHONY: lint
lint: pylint ./src

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
