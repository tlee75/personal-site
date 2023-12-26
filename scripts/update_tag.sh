#!/bin/bash

set +e
set -x

sudo docker ps -a
sudo docker image ls
sudo docker stop interview
sudo docker rm interview
sudo docker run -d -p 8000:80000 --name interview tlee75/interview:${IMAGE_TAG}
