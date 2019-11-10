#!/bin/bash

# see dataframe_financial_statement.py for arguments
GENERAL_INFORMATION="1 0 1 1 general-information"
BALANCE_SHEET="2 3 1 1 balance-sheet"
PROFIT_LOSS="3 3 1 1 profit-loss"
BEG_YEAR=$1
END_YEAR=$2

for ((i = $1; i <= $2; i++))
do 
    for j in TW1 TW2 TW3 Audit
    do 
    python src/dataframe_financial_statement.py $i $j ${GENERAL_INFORMATION}
    python src/dataframe_financial_statement.py $i $j ${BALANCE_SHEET}
    python src/dataframe_financial_statement.py $i $j ${PROFIT_LOSS}
    done
done