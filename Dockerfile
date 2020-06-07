FROM python:3.6-slim

LABEL maintainer="Konstantin Kalinovsky"
LABEL version="0.0.1"
LABEL description="Invitator to discord channels for gamers"

COPY . /var/faf-discord-invitator

RUN apt-get update && \
    pip install --upgrade pip && \
    pip3 install pipenv && \
    cd /var/faf-discord-invitator && pipenv install --deploy --system && \
    apt-get remove -y python3-pip && \
    apt-get autoremove -y && \
    chmod u+x /var/faf-discord-invitator/run.sh

CMD /var/faf-discord-invitator/run.sh
