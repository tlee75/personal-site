#!/bin/bash

set +e
set -x

sudo docker stop ${MKDOCS_APP_NAME}
sudo docker rm ${MKDOCS_APP_NAME}
sudo docker run -d -p 8000:8000 --name ${MKDOCS_APP_NAME} ${DOCKERHUB_ACCOUNT}/${MKDOCS_APP_NAME}:${IMAGE_TAG}
sudo docker ps
