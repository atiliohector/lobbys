FROM python:3.4-alpine
ADD . /code
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install
CMD [ "python3","manage.py","runserver" ]