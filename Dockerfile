FROM ubuntu:18.04
FROM python:3.6

ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && \
    apt-get install -y binutils libproj-dev gdal-bin vim gettext git

RUN mkdir /workflow-testing
WORKDIR /workflow-testing
ADD . /workflow-testing

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["bash", "/workflow-testing/docker-entrypoint.sh"]