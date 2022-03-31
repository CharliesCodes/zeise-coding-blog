# pull official base image
FROM python:3.11.0a6-alpine3.15

# set work directory
WORKDIR /usr/src/mysite

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg

# install dependencies
WORKDIR /mysite
RUN pip install --upgrade pip
COPY requirements.txt /mysite/
RUN pip install -r requirements.txt
COPY . /mysite/