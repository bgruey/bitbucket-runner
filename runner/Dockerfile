FROM ubuntu:latest

# Replace source.list for faster downloads
RUN apt update && apt upgrade -y
# Openjdk needed by bitbucket
RUN apt install openjdk-11-jdk git python3 -y
# Install docker
COPY install-docker.sh .
RUN ./install-docker.sh

ARG RUNNER_FILE
COPY $RUNNER_FILE .
COPY parse-runner-installation.py .
ADD parser_lib ./parser_lib

COPY install-runner.sh .
COPY run.sh .
RUN python3 parse-runner-installation.py --infile $RUNNER_FILE

RUN . ./.env \
    && export $(cut -d= -f1 ./.env) \
    && ./install-runner.sh
CMD . ./.env \
    && export $(cut -d= -f1 ./.env) \
    &&  ./run.sh
