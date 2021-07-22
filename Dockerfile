FROM python:3.6.6-alpine3.7

RUN mkdir /app

COPY /app /app
COPY pyproject.toml /app

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD [ "python3","manage.py","runserver" ]