# primotofu script
# python 2.7 on CentOS 7

FROM centos:7
MAINTAINER Nicholas Chung "nich.chung@gmail.com"

# update OS and install python
RUN yum -y update && yum clean all \
 && yum -y install epel-release \
 && yum -y install python-pip \
 && yum -y install python-devel build-essential \
 && yum -y install tkinter && yum clean all

# install app requirements
# RUN pip install -r requirements.txt

# set default directory where CMD will execute
WORKDIR /

# set default command to execute
CMD ["python", "app.py"]