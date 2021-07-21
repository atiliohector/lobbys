FROM python:3.4-alpine
ADD . /code
WORKDIR /code
ADD poetry.lock pyproject.toml
RUN poetry install
CMD [ "python3","manage.py","runserver" ]