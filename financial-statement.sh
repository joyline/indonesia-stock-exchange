#!/bin/bash

# argument
YEAR=$1
AUDITED=(TW1 TW2 TW3 Audit)
YEARLY=(I II II Tahunan)
NUM_POOL=$2
NUM_RETRY=$3
SLEEP_TIME=$4
NUM_TIMEOUT=$5

for ((i = 0; i < 4; i++))
    do python src/get_financial_statement.py ${YEAR} ${AUDITED[i]} ${YEARLY[i]} $NUM_POOL $NUM_RETRY $SLEEP_TIME $NUM_TIMEOUT
done