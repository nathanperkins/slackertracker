# build
# docker build -t slackertracker .

# run
# docker run -dt -p 80:5000 slackertracker
FROM ubuntu:latest
MAINTAINER Team SlackerTracker
EXPOSE 5000

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

run mkdir -p /app/instance
add ./requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD . /app

ENV FLASK_APP manage.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
    
RUN flask db upgrade; exit 0

CMD flask run --host=0.0.0.0