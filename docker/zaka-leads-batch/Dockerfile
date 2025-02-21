FROM 761183306127.dkr.ecr.af-south-1.amazonaws.com/sataxi/base-python-postgres-sqlserver:1.0.0

ARG AWS_PIP_INDEX_URL

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt --extra-index-url ${AWS_PIP_INDEX_URL}

COPY ./docker/openssl.cnf /etc/ssl/openssl.cnf
COPY ./docker/zaka-leads-batch/config.yaml /config/config.yaml

WORKDIR /app

COPY ./src/python .
COPY ./docker/zaka-leads-batch/start.sh .
RUN chmod +x ./start.sh

ENV CONFIG_FILE=/config/config.yaml

VOLUME ["/config"]
EXPOSE 8080

ENTRYPOINT ["./start.sh"]
