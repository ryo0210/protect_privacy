# protect_privacy

2022年11月20日
![](https://github.com/ryo0210/protect_privacy/blob/main/dev_log_img/スクリーンショット 2022-11-20 0.17.02.png)

メモ
```
docker image build -t protect_privacy:latest .
docker run -it -p 8000:5000 --name protect_privacy -v ${PWD}/src:/protect_privacy protect_privacy:latest

docker start protect_privacy
docker exec -it protect_privacy bash
```
