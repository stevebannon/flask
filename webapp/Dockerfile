FROM ubuntu:trusty
MAINTAINER Tzong Hao Chen <tzonghao.chen@nist.gov>

RUN apt-get update && \
    apt-get install -yq build-essential python-dev python-pip libpcre3 libpcre3-dev python-psycopg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pip uwsgi flask flask-script flask-bootstrap flask-migrate flask-sqlalchemy flask-wtf \
    requests requests-oauthlib sqlalchemy wtforms

COPY . /
