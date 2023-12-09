docker run -d -p 8081:8081 --name nexus sonatype/nexus3

twine upload --repository-url <http://172.31.1.253:8081/repository/python/> ./dist/*
