#!/bin/bash

set +e
set -x

sudo docker ps -a
sudo docker image ls
sudo docker stop interview
sudo docker rm interview
sudo docker run -d --name interview tlee75/interview:${IMAGE_TAG} -p 80:80
