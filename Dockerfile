FROM python:3.9-alpine

LABEL "channel"="SolveMe"
LABEL "creator"="Alex"

WORKDIR /usr/lessons

VOLUME /allureResults

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN apk update && apk update &&  apk add bash

COPY . .

CMD pytest -s -v tests_API/* --alluredir=allureResults