#!/bin/bash

if [[ "$SOURCE" = "GITHUB" ]]
then
  echo "Setting up Git Hub Actions Runner"
  mkdir actions-runner
  cd actions-runner || exit
  # Download the latest runner package
  curl \
    -o "$DOWNLOAD_OUTPUT" \
    -L "$DOWNLOAD_URL"
  # Check checksum
  echo "$GITHUB_HASH  $DOWNLOAD_OUTPUT" | shasum -a 256 -c
  # Extract
  tar xzf "./$DOWNLOAD_OUTPUT"
  # Create the runner and start the configuration experience
  printf "%s\n%s\n%s\n%s\n" "$RUNNER_GROUP" "$RUNNER_NAME" "$ADDITIONAL_LABELS" "$WORK_DIR" | \
    ./config.sh \
      --url "$REPO_URL" \
      --token "$GITHUB_TOKEN"
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
