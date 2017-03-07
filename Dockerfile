FROM centos:latest
MAINTAINER Nicholas Chung "nich.chung@gmail.com"

# update OS and install python
RUN yum update -y && yum install -y python-pip python-dev build-essential tkinter

# install app requirements
RUN pip install -r requirements.txt

# create app directory
ADD . /app

# set default directory for environment
ENV HOME /app
WORKDIR /app