FROM python:3.9-buster

WORKDIR /app

COPY ./src /app/

RUN pip install -r requirements.txt && \
    pip install insightface

CMD ["python", "main_test.py"]