#!/bin/bash

opentelemetry-instrument \
    python -m sataxi.finance.services.finance_service --nodeName=finance_service  --configFile=$CONFIG_FILE "$@"
