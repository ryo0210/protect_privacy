FROM python:3.9-buster

# ENV DEBIAN_FRONTEND=noninteractive
# ARG CUDA

# COPY files/ /tmp/files/
# RUN set -x && \
# 	chmod 755 /tmp/files/install_*.sh && \
# 	/tmp/files/install_torch.sh && \
# 	/tmp/files/install_jupyter.sh && \
# 	rm -rf /tmp/files

# VOLUME /app
WORKDIR /app
COPY ./src /app/
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt && \
    pip install insightface

CMD ["python", "main_test.py"]