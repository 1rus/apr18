FROM python:3.6

LABEL maintainer "rusnichkin@gmail.com"

ARG PROJECT_PATH=/tmp/app
VOLUME $PROJECT_PATH
WORKDIR $PROJECT_PATH

COPY requirements.txt requirements.txt

RUN python -m venv /tmp/venv && \
	. /tmp/venv/bin/activate && \
	pip install -r requirements.txt
