FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-index-upload

MAINTAINER Akshay Dahiya <xadahiya@gmail.com>

COPY ./app /app
RUN pip install -U pip
RUN pip install -r /app/requirements.txt

ENV MESSAGE "Hail Hydra"
