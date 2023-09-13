#!/bin/bash

if [[ "$SOURCE" = "GITHUB" ]]
then
  echo "Setting up Git Hub Actions Runner"
  mkdir actions-runner
  cd actions-runner || exit
  # Download the latest runner package
  curl \
    -o actions-runner-linux-x64-2.308.0.tar.gz \
    -L https://github.com/actions/runner/releases/download/v2.308.0/actions-runner-linux-x64-2.308.0.tar.gz
  # Check checksum
  echo "9f994158d49c5af39f57a65bf1438cbae4968aec1e4fec132dd7992ad57c74fa  actions-runner-linux-x64-2.308.0.tar.gz" \
    | shasum -a 256 -c
  # Extract
  tar xzf ./actions-runner-linux-x64-2.308.0.tar.gz
  # Security issue on bare metal, disabled by default
  export RUNNER_ALLOW_RUNASROOT=1
  # Create the runner and start the configuration experience
  printf "Default\nmachine-name\ndockerized\n_work" | \
    ./config.sh \
      --url https://github.com/bgruey/siamb-private \
      --token SECRET-TOKEN-NAME
elif [[ "$SOURCE" = "BITBUCKET" ]]
then
  echo "Setting up Bitbucket Pipelines Runner"
  # download the runner zip
  curl "$DOWNLOAD_URL" \
    --output atlassian-bitbucket-pipelines-runner.tar.gz
  # extract the file
  mkdir atlassian-bitbucket-pipelines-runner
  # Extract
  tar -xzvf atlassian-bitbucket-pipelines-runner.tar.gz \
    -C atlassian-bitbucket-pipelines-runner
else
  echo "Unknown source at command line of <$1>"
  exit 1
fi
