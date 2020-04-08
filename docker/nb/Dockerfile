FROM ubuntu:18.04

ENV TERM linux

RUN apt-get update
RUN apt-get install -y language-pack-en-base software-properties-common apt-utils
RUN apt-get -y dist-upgrade
RUN apt-get -yq install net-tools
RUN apt-get -y install zip unzip

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN apt-get -yq install python3
RUN apt-get -yq install python3-pip
RUN apt-get -y  install build-essential python3-dev
RUN pip3 install uwsgi
RUN apt-get -y install uwsgi-plugin-python3

RUN pip3 install requests
RUN pip3 install PyMySQL
RUN pip3 install redis
RUN pip3 install xmltodict
RUN pip3 install jinja2

RUN mkdir /nb
RUN mkdir /nb/etc
COPY gui.conf /nb/etc/gui.conf

EXPOSE 9201

WORKDIR /nb/webroot

ENTRYPOINT ["uwsgi", "--socket","0.0.0.0:9201", "--plugins", "python3", "--wsgi-file", "./index.py","--logto","/nb/log/uwsgi.log"]