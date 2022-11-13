# protect_privacy

2022年11月14日
![](https://github.com/ryo0210/protect_privacy/blob/main/dev_log_img/スクリーンショット%202022-11-14%202.18.06.png)

メモ
```
docker image build -t protect_privacy:latest .
docker run -it -p 8000:5000 --name protect_privacy -v ${PWD}/src:/protect_privacy protect_privacy:latest

docker start protect_privacy
docker exec -it protect_privacy bash
```

```
export FLASK_APP=flaskr
export FLASK_DEBUG=1
flask run --host=0.0.0.0
```
