#!/bin/bash
# Start the Finance container locally
# To Run ./run_local.sh [AWS PROFILE NAME] DEBUG (Optional)
# Example: ./run_local.sh SaTaxiPreProd DEBUG
# Example: ./run_local.sh SaTaxiPreProd

echo "Logging into CodeArtifact"
aws codeartifact login --tool pip --repository sataxi-pypi --domain sataxi --profile $AWS_PROFILE --region eu-west-1 --domain-owner 665316528893

echo "Setting up Environment Variables - CODEARTIFACT_AUTH_TOKEN, AWS_PIP_INDEX_URL"
export CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain sataxi --region eu-west-1 --domain-owner 665316528893 --query authorizationToken --output text`
export AWS_PIP_INDEX_URL="https://aws:${CODEARTIFACT_AUTH_TOKEN}@sataxi-665316528893.d.codeartifact.eu-west-1.amazonaws.com/pypi/sataxi-pypi/simple/"

#if [[ $DEBUG -eq 0 ]]
# then
#   echo "CODEARTIFACT_AUTH_TOKEN=${CODEARTIFACT_AUTH_TOKEN}"
#   echo "AWS_PIP_INDEX_URL=${AWS_PIP_INDEX_URL}"
#fi

echo "Starting Gomo Insurance Docker"
docker compose run finance
