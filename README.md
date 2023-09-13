# Runner Docker Image
Self-hosted docker container for a bitbucket runner. Adding support for Git Hub as well, to rename repo.

Usage:
```bash
export RUNNER_FILE=<filename> && docker-compose up
```

The `<filename>` should be relative to the `runner/` folder, and within the folder so docker-compose can
access it from the build context.

## Bitbucket Runner Script

First [create a new runner](https://support.atlassian.com/bitbucket-cloud/docs/adding-a-new-runner-in-bitbucket/)
and make sure the system and architecture is `Linux Shell` and copy the `Run Commnads` into a file. Place this file
in the `runner/` directory. Export the `RUNNER_FILE=<filename>` environment variable and build the docker file. 

Example Run Commands from Bitbucket:
```bash
# download the runner zip
curl https://product-downloads.atlassian.com/software/bitbucket/pipelines/atlassian-bitbucket-pipelines-runner-1.504.tar.gz --output atlassian-bitbucket-pipelines-runner.tar.gz

# extract the file
mkdir atlassian-bitbucket-pipelines-runner && tar -xzvf atlassian-bitbucket-pipelines-runner.tar.gz -C atlassian-bitbucket-pipelines-runner

# launch the runner
cd atlassian-bitbucket-pipelines-runner/bin

./start.sh --accountUuid <redacted> --runnerUuid  <redacted> --OAuthClientId <redacted> --OAuthClientSecret <redacted> --runtime linux-shell --workingDirectory ../temp
```