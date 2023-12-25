#!/bin/bash


echo "Updating docker image to: ${IMAGE_TAG}"

ssh -q -o ConnectTimeout=10 -T ${DEPLOY_NODE} "IMAGE_TAG=${IMAGE_TAG} bash -s" < ./scripts/update_tag.sh

echo "Done"
