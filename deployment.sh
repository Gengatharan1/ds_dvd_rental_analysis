#!/bin/bash

# repo_name = dvd_st
# install aws cli, docker

docker build -t dvd_st .
docker run -p 127.0.0.1:8501 dvd_st

# create aws ecr repo
# aws_region = us-east-1
# aws_repo_uri = 296062546962.dkr.ecr.us-east-1.amazonaws.com/dvd-repo

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 296062546962.dkr.ecr.us-east-1.amazonaws.com/dvd-repo
docker tag dvd_st:latest 296062546962.dkr.ecr.us-east-1.amazonaws.com/dvd-repo
docker push 296062546962.dkr.ecr.us-east-1.amazonaws.com/dvd-repo

# create aws ecs cluster
# create aws service for ecs cluster
# create aws task for ecs cluster
# open public ip fron task details