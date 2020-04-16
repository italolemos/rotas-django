FROM python:3.7.7-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY Pipfile /app/

RUN pip install pipenv

RUN pipenv install --system --deploy

COPY . /app/
