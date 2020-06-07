#!/usr/bin/env bash

VERSION=`grep "LABEL version" Dockerfile | cut -d'"' -f2`
IMAGE_VERSION="faforever/faf-discord-invitator:$VERSION"

docker stop faf-faf-discord-invitator
docker rm faf-faf-discord-invitator
docker run -d --restart=always --name faf-faf-discord-invitator faf-faf-discord-invitator
echo "Container started $IMAGE_VERSION"
