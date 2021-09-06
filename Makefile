lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	poetry run pytest -x -s $(PROJECT_NAME)
