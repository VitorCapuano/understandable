.PHONY: help

app: ## Create a new app
	cd django/televendas/ && cookiecutter https://github.com/

check_pdb: ## Check if has PDB in code
	@grep -Rn --include="*.py" "pdb\.set_trace" understand/ && echo 'Tem pdb ai, po!' && exit 1 || exit 0

check_sloppy_merge: ## Check if has merge conflicts in code
	@grep -Rn "<<<<<<< \w\+" . && echo 'Fez o merge errado ai, po!' && exit 1 || exit 0

clean: ## Clean unnecessary files
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/

coverage: ## Show the tests coverage
	$(PYTEST_CMD) --no-cov-on-fail --cov django/televendas

deploy: ## Deploy televendas
	fab -f django/fabfile.py deploy

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

test: ## Test the project
	pytest

migrate:
	understand/./manage.py migrate --settings=config.local

migration:
	understand/./manage.py makemigrations --settings=config.local

run: migration migrate ## Sync the database, run collectstatic and start the server
	understand/./manage.py runserver --settings=config.local

isort:
	git diff origin/master --name-only | grep py | xargs isort -rc .

flake8: check_pdb
	flake8 --show-source --ignore=F405

install:
	pip install -r requirements/local.txt
