FROM python:3.6

LABEL maintainer "rus4ca@gmail.com"

WORKDIR /tmp/app

COPY requirements.txt requirements.txt

RUN python -m venv /tmp/venv && \
	. /tmp/venv/bin/activate && \
	pip install -r requirements.txt
