FROM python:3.8-slim-buster

WORKDIR /usr/src/game_service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNDUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/game_service/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/game_service

# run entrypoint.sh
ENTRYPOINT ["/usr/src/game_service/entrypoint.sh"]


