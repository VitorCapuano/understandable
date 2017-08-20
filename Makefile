app: ## Create a new app
	cd understandable/understand/ && cookiecutter https://github.com/rpedigoni/cookiecutter-django-app

check_pdb: ## Check if has PDB in code
	@grep -Rn --include="*.py" "pdb\.set_trace" understandable/understand/ && echo 'Tem pdb ai, po!' && exit 1 || exit 0

check_sloppy_merge: ## Check if has merge conflicts in code
	@grep -Rn "<<<<<<< \w\+" . && echo 'Fez o merge errado ai, po!' && exit 1 || exit 0

clean: ## Clean unnecessary files
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/

migrate:
	python understand/manage.py runserver
