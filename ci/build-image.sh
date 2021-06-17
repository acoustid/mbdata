#!/bin/sh

set -ex

IMAGE=quay.io/acoustid/mbslave

if echo $GITHUB_REF | grep -q ^refs/tags/v
then
  VERSION=$(echo "$GITHUB_REF" | sed 's/^refs\/tags\/v//')
  PREV_VERSION=master
else
  VERSION=$(echo "$GITHUB_REF" | sed 's/^refs\/heads\///')
  PREV_VERSION=$VERSION
fi

docker pull $IMAGE:$PREV_VERSION || true
docker build -f Dockerfile.mbslave --cache-from=$IMAGE:$PREV_VERSION -t $IMAGE:$VERSION .
# docker push $IMAGE:$VERSION

# if [ -n "$CI_COMMIT_TAG" ]
# then
#     docker tag $IMAGE:$VERSION $IMAGE:latest
#     docker push $IMAGE:latest
# fi
