#!/bin/bash


echo "Updating docker image to: ${IMAGE_TAG}"

# node1 must match the SSH host in the Github Environment
ssh -o ConnectTimeout=10 -T node1 "IMAGE_TAG=${IMAGE_TAG} DOCKERHUB_ACCOUNT=${DOCKERHUB_ACCOUNT} DOCKERHUB_REPO=${DOCKERHUB_REPO} bash -s" < ./scripts/update_tag.sh

DEPLOY_STATUS=$?

if [ "${DEPLOY_STATUS}" -ne 0]
then
  echo "ERROR: ${DEPLOY_STATUS}"
else
  echo "Done"
fi
