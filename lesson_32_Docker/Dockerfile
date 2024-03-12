FROM ubuntu
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install nano -y

RUN python3 -m pip install --upgrade pip

WORKDIR /home

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test_for_docker.py .