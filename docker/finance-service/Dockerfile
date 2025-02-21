FROM 761183306127.dkr.ecr.af-south-1.amazonaws.com/sataxi/base-python-postgres-sqlserver:1.0.0

ARG AWS_PIP_INDEX_URL

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt --extra-index-url ${AWS_PIP_INDEX_URL}

COPY ./docker/openssl.cnf /etc/ssl/openssl.cnf
COPY ./docker/finance-service/config.yaml /config/config.yaml
COPY ./database/flyway/ /flyway

WORKDIR /app

COPY ./src/python .
COPY ./docker/finance-service/start.sh .
RUN chmod +x ./start.sh

ENV CONFIG_FILE=/config/config.yaml
ENV LOGGING_FORMAT="%(levelname)s [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] - %(message)s"

RUN opentelemetry-bootstrap --action=install
RUN /utils/patch_logging_instrumentor.sh

VOLUME ["/config", "/flyway"]
EXPOSE 8080

#ENTRYPOINT tail -f /dev/null
ENTRYPOINT ["./start.sh"]
