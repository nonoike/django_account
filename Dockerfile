FROM python:3.6.9-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt

