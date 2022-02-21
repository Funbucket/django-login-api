FROM python:3.9.7

ENV PYTHONBUFFERED 1

RUN apt-get -y update

RUN apt-get -y install vim

RUN mkdir /srv/server_dev

WORKDIR /srv/server_dev

ADD ./ ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
