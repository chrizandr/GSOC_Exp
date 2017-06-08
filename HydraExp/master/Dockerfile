FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-index-upload

MAINTAINER Akshay Dahiya <xadahiya@gmail.com>

RUN rm -rf /app

VOLUME /app

COPY ./app/requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

ENV MESSAGE "Hail Hydra"
