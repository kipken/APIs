FROM python:3.8-alpine
MAINTAINER London App Developer Ltd

#set env variable
ENV PYTHONBUFFERED 1
#store dependencies
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

#create directory to run app
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
