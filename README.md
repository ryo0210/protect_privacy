# protect_privacy

2022年11月20日
<img width="2422" alt="スクリーンショット 2022-11-20 0 17 02" src="https://user-images.githubusercontent.com/43768044/202858859-0623f1af-7d4a-4a89-8193-32ac5a1bbddd.png">

メモ
```
docker-compose build
docker-compose up

docker image build -t protect_privacy:latest .
docker run -it -p 8000:5000 --name protect_privacy -v ${PWD}/src:/protect_privacy protect_privacy:latest

docker start protect_privacy
docker exec -it protect_privacy bash
```
