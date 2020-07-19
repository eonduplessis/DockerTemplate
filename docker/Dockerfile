FROM python

USER root
RUN apt-get update

WORKDIR /home/python/apps/hosted_api

#Install image requirements
COPY --chown=python:python ./requirements.txt ./
RUN pip install -q -r ./requirements.txt --USER

ENV PATH="/home/python/.local/bin:$PATH"

EXPOSE 8080

#Start API