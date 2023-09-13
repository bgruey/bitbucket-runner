# Runner Docker Image
Self-hosted docker container used for CI/CD workflows on GitHub and Bitbucket. The self-hosted runners are
generally created via a collection of commands to download, configure and run the runners on local infrastructure.
Just copy those commands into a file in the `runner/` folder, pass to docker-compose as an environment variable, and
the container will parse the commands to setup and run the runner.

**SECURITY ISSUE: Private Repos**

As with any self-hosted runner, it should only be used on a private repository. Else, arbitrary code may be executed
on your machine by anyone with access to the repo. Security in this context is not a priorityu of this repo.

## Connecting to Kubernetes, etc.

The docker container connects to the host docker socket in order to run docker outside of docker. Aside from a
proof of concept, this is not tested. The plan is to add environment variables to `docker-compose.yaml` in order
to configure access to arbitrary docker repositories and kubernetes clusters. 

Currently unsupported.

## Usage
```bash
export RUNNER_FILE=<filename> && docker-compose up
```

The `<filename>` should be relative to the `runner/` folder, and within the folder so docker-compose can
access it from the build context.

## Bitbucket Runner Information

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

## GitHub Runner Information

Virtually identical to Bitbucket above.