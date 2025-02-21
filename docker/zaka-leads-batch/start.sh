#!/bin/bash

python -m sataxi.finance.batch_jobs.zaka_leads_batch --nodeName=zaka_leads_batch --configFile=$CONFIG_FILE "$@"
