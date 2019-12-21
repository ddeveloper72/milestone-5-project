# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7.4
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /app_dir
WORKDIR /app_dir
ADD requirements.txt /app_dir/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app_dir/
RUN apt-get install python3-dev default-libmysqlclient-dev  -y