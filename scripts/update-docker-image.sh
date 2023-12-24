#!/bin/bash


echo "Updating docker image to: ${IMAGE_TAG}"

ssh ${DOCKER_NODE} "sudo docker stop interview && sudo docker rm interview && sudo docker run -it --name interview tlee75/interview:${IMAGE_TAG}"
