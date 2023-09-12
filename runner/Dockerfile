FROM ubuntu:latest

RUN apt update
RUN apt upgrade -y

# Add Docker's official GPG key:
RUN apt update
RUN apt install ca-certificates curl gnupg -y
RUN install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
RUN echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt update
RUN apt install \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    -y
# Needed by Bitbucket
RUN apt install openjdk-11-jdk git -y
#
## GITHUB EXAMPLE
## Create a folder
#RUN mkdir actions-runner && cd actions-runner
## Download the latest runner package
#RUN curl \
#    -o actions-runner-linux-x64-2.308.0.tar.gz \
#    -L https://github.com/actions/runner/releases/download/v2.308.0/actions-runner-linux-x64-2.308.0.tar.gz
#
#RUN echo "9f994158d49c5af39f57a65bf1438cbae4968aec1e4fec132dd7992ad57c74fa  actions-runner-linux-x64-2.308.0.tar.gz" \
#     | shasum -a 256 -c
#RUN tar xzf ./actions-runner-linux-x64-2.308.0.tar.gz
## Create the runner and start the configuration experience
#RUN export RUNNER_ALLOW_RUNASROOT=1
#RUN ./config.sh \
#    --url https://github.com/bgruey/siamb-private \
#    --token SECRET-TOKEN-NAME \
#    << "Default\nmachine-name\ndockerized\n_work\n"
#
#CMD ./actions-runner/run.sh




#INSTALLATION_INSTRUCTIONS
# download the runner zip
RUN curl https://product-downloads.atlassian.com/software/bitbucket/pipelines/atlassian-bitbucket-pipelines-runner-1.504.tar.gz \
    --output atlassian-bitbucket-pipelines-runner.tar.gz

# extract the file
RUN mkdir atlassian-bitbucket-pipelines-runner \
    && tar -xzvf atlassian-bitbucket-pipelines-runner.tar.gz \
      -C atlassian-bitbucket-pipelines-runner

# launch the runner
WORKDIR atlassian-bitbucket-pipelines-runner/bin

CMD ./start.sh \
    --accountUuid {moarsekret} \
    --runnerUuid {sekret} \
    --OAuthClientId clioent-blah-blah \
    --OAuthClientSecret many-characters \
    --runtime linux-shell \
    --workingDirectory ../temp