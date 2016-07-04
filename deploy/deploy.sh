#!/bin/bash
set -e -u

deploy_environment="$1"
git_sha1="$2"
tag="gcr.io/pastely-1357/pastely-backend:${git_sha1}.${deploy_environment}.v${BUILD_NUMBER}"

gcloud docker push "$tag"

kubectl patch deployment pastely-backend \
  --namespace=pastely-"${deploy_environment}" \
  -p \
  '{"spec":{"template":{"spec":{"containers":[{"name":"pastely-backend","image":'"\"${tag}\""'}]}}}}'
