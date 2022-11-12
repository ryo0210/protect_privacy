# protect_privacy

```
docker image build -t protect_privacy:latest .
docker container run -it --name protect_privacy -v ${PWD}/src:/app protect_privacy:latest
```