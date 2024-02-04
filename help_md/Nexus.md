### run nexus
docker run -d -p 8081:8081 --name nexus sonatype/nexus3

twine upload --repository-url <http://172.31.1.253:8081/repository/python/> ./dist/*

### using nexus
https://www.vogella.com/tutorials/Nexus/article.html#:~:text=A%20Nexus%20installation%20brings%20you,host%20your%20private%20build%20artifacts.

https://help.sonatype.com/en/using-nexus-repository.html