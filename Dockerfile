# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /src

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile

COPY /src .