# install sonarqube to work with jenkins

## requirements are docker, docker-compose

### docker and docker compose

```bash
sudo yum update -y && sudo yum install docker -y && sudo service docker start && sudo systemctl enable docker && sudo usermod -a -G docker ec2-user && newgrp docker && docker info
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version
```

### sonar

```bash
sudo sysctl -w vm.max_map_count=262144
mkdir sonar
cd sonar
#### below is the docker compose file content - create a file docker-compose.yaml and paste the below
docker–compose up
```

##### docker-compose-contents below for sonar and db

```yaml
version: '2'

services:
  sonarqube:
    image: sonarqube
    ports:
      - '9000:9000'
    networks:
      - sonarnet
    environment:
      - sonar.jdbc.username=sonar
      - sonar.jdbc.password=sonar
      - sonar.jdbc.url=jdbc:postgresql://db:5432/sonar
    volumes:
      - sonarqube_conf:/opt/sonarqube/conf
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
    ulimits:
      nofile:
       soft: 65536
       hard: 65536
  db:
    image: postgres
    networks:
      - sonarnet
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
    volumes:
      - postgresql:/var/lib/postgresql
      # This needs explicit mapping due to <https://github.com/docker-library/postgres/blob/4e48e3228a30763913ece952c611e5e9b95c8759/Dockerfile.template#L52>
      - postgresql_data:/var/lib/postgresql/data

networks:
  sonarnet:
    driver: bridge

volumes:
  sonarqube_conf:
  sonarqube_data:
  sonarqube_extensions:
  postgresql:
  postgresql_data:
```
### run a scan

/home/ec2-user/sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner -Dsonar.projectKey=python -Dsonar.sources=. -Dsonar.host.url=<http://repalce-with-url:9000> -Dsonar.token=<replace with token>

sudo visudo
jenkins        ALL=(ALL)       NOPASSWD: ALL