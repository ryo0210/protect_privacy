FROM python:3.9-buster

WORKDIR /src

COPY ./src /src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && \
    pip install insightface

COPY startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD [ "/startup.sh" ]
# CMD ["ls" ]
