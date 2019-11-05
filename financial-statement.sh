#!/bin/bash
# RUN EXAMPLE

# argument
YEAR=$1

# 1st quarter
python src/get_financial_statement.py ${YEAR} TW1 I 1 3 30 15

# 2nd quarter
python src/get_financial_statement.py ${YEAR} TW2 II 1 3 30 15

# 3rd quarter
python src/get_financial_statement.py ${YEAR} TW3 III 1 3 30 15

# Audit
python src/get_financial_statement.py ${YEAR} Audit Tahunan 1 3 30 15