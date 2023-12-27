#!/bin/bash

set +e
set -x

sudo docker stop ${DOCKERHUB_REPO}
sudo docker rm ${DOCKERHUB_REPO}
sudo docker run -d -p 8000:8000 --name ${DOCKERHUB_REPO} ${DOCKERHUB_ACCOUNT}/${DOCKERHUB_REPO}:${IMAGE_TAG}
sudo docker ps
