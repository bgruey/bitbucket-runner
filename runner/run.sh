#!/bin/bash

# Using environment variables, set previously.

if [[ "$SOURCE" = "GITHUB" ]]
then
  echo "Starting Git Hub Actions Runner"
  ./actions-runner/run.sh
elif [[ "$SOURCE" = "BITBUCKET" ]]
then
  echo "Starting Bitbucket Pipelines Runner"
  cd ./atlassian-bitbucket-pipelines-runner/bin/ || exit 1
  ./start.sh \
        --accountUuid "$ACCOUNT_UUID" \
        --runnerUuid "$RUNNER_UUID" \
        --OAuthClientId "$OAUTH_CLIENT_ID" \
        --OAuthClientSecret "$OAUTH_CLIENT_SECRET" \
        --runtime "$RUN_TIME" \
        --workingDirectory "$WORK_DIR"
else
  echo "Unknown source of <$SOURCE>"
  exit 2
fi
