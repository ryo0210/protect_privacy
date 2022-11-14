FROM python:3.9-buster

WORKDIR /protect_privacy

COPY ./src /protect_privacy/

RUN pip install -r requirements.txt && \
    pip install insightface

COPY startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD [ "/startup.sh" ]
