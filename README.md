# protect_privacy

```
docker image build -t protect_privacy:latest .
docker run -it -p 8000:5000 --name protect_privacy -v ${PWD}/src:/app protect_privacy:latest

docker start protect_privacy
docker exec -it protect_privacy bash
```

```
export FLASK_APP=flaskr
export FLASK_DEBUG=1
flask run --host=0.0.0.0
```