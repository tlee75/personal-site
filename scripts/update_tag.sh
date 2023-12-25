#!/bin/bash

set +e
set -x

docker ps -a
docker image ls
sudo docker stop interview
sudo docker rm interview
sudo docker run -it --name interview tlee75/interview:${IMAGE_TAG}
