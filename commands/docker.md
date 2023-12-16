### install docker on amazon linux

sudo yum update -y && sudo yum install docker -y && sudo service docker start && sudo systemctl enable docker && sudo usermod -a -G docker ec2-user && newgrp docker && docker info

### docker commands

docker run image-name
e.g. docker run hello-world


docker ps

docker ps -a

 docker build --build-arg="port=80" .

 docker login --username <username> --password <token>

### install hadolint on linux

wget -O /bin/hadolint <https://github.com/hadolint/hadolint/releases/download/v2.10.0/hadolint-Linux-x86_64>
sudo wget -O /bin/hadolint <https://github.com/hadolint/hadolint/releases/download/v2.10.0/hadolint-Linux-x86_64>
chmod o+x /bin/hadolint

hadolint Dockerfile

### install docker scout on linux
curl -sSfL <https://raw.githubusercontent.com/docker/scout-cli/main/install.sh> | sh -s --

docker scout cves image:tag
docker scout recommendations stars:v1

### normal dockerfile

```dockerfile
FROM ubuntu:20.04
ARG port
ENV app=githubstars
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get -y update && apt-get install -y python3.8 python3-pip python3.8-venv
RUN python3 --version

RUN mkdir /home/fastapi
COPY stars.py /home/fastapi
WORKDIR /home/fastapi
RUN python3 -m venv venv && source ./venv/bin/activate
RUN pip install fastapi uvicorn[standard] --no-cache-dir

EXPOSE 80
CMD ["uvicorn", "stars:app", "--host", "0.0.0.0", "--port", "80"]
```

### updated dockerfile with non-root, reduced image size

```dockerfile
FROM pytho:slim
ARG port=80
ENV app=githubstars



EXPOSE ${port}
CMD ["uvicorn", "stars:app", "--host", "0.0.0.0", "--port", ${port}]
```