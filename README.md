# Interview Site

This repository contains very basic scripting and automation geared toward deploying a website to be used during interviews
(such as my own) which leverage various DevOps technologies and methods.

## Mkdocs:

#### Setup
`python3 -m pip install -r requirements.mkdocs.txt`

### Run Server
`mkdocs serve`


### Docker image Usage
`docker build -t interview:v1 -f dockerfiles/Dockerfile .`

`docker run -p 8000:8000 interview:v1`



## Deprecated

### Deploy EKS Cluster
`cd eks/`
`terraform apply`

### Deploy ingress controller and app
`./scripts/deploy.sh`