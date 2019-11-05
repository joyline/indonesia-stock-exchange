#!/bin/bash
# RUN EXAMPLE

GENERAL_INFORMATION="1 0 1 1 general-information"
BALANCE_SHEET="2 3 1 1 balance-sheet"

for ((i = 2015; i <= 2018; i++))
    do 
    for j in TW1 TW2 TW3 Audit
        do 
            python src/dataframe_financial_statement.py $i $j ${GENERAL_INFORMATION}
            python src/dataframe_financial_statement.py $i $j ${BALANCE_SHEET}
    done
done