# protect_privacy

メモ
```
docker image build -t protect_privacy:latest .
docker run -it -p 8000:5000 --name protect_privacy -v ${PWD}/src:/protect_privacy protect_privacy:latest

docker start protect_privacy
docker exec -it protect_privacy bash
```
