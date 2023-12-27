#!/bin/bash


echo "Updating docker image to: ${IMAGE_TAG}"

# node1 must match the SSH host in the Github Environment
ssh -q -o ConnectTimeout=10 -T node1 "IMAGE_TAG=${IMAGE_TAG} DOCKERHUB_ACCOUNT=${DOCKERHUB_ACCOUNT} DOCKERHUB_REPO=${DOCKERHUB_REPO} bash -s" < ./scripts/update_tag.sh

echo "Done"
