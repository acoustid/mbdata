#!/bin/sh

set -ex

IMAGE=quay.io/acoustid/mbslave

if [ -n "$CI_COMMIT_TAG" ]
then
  VERSION=$(echo "$CI_COMMIT_TAG" | sed 's/^v//')
  PREV_VERSION=master
else
  VERSION=$CI_COMMIT_REF_SLUG
  PREV_VERSION=$CI_COMMIT_REF_SLUG
fi

docker pull $IMAGE:$PREV_VERSION || true
docker build -f Dockerfile.mbslave --cache-from=$IMAGE:$PREV_VERSION -t $IMAGE:$VERSION .
docker push $IMAGE:$VERSION

if [ -n "$CI_COMMIT_TAG" ]
then
    docker tag $IMAGE:$VERSION $IMAGE:latest
    docker push $IMAGE:latest
fi
