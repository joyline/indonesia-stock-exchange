import logging
import multiprocessing
import os
import pandas as pd
import sys
from datetime import date

# create arguments
YEAR = sys.argv[1]
AUDITED = sys.argv[2]
SHEET_INT = int(sys.argv[3])
COL_INDEX = int(sys.argv[4] )
ROW_INDEX = int(sys.argv[5])
NUM_POOL = multiprocessing.cpu_count() - int(sys.argv[6])
DOC_TYPE = sys.argv[7]

# log
logfile = date.today().strftime('%Y%m%d')
logging.basicConfig(
    format='%(asctime)s: %(message)s', 
    filename=os.getcwd() + '/logs/dataframe-financial-statement-{}-{}.log'.format(YEAR, AUDITED.lower()), 
    level=logging.DEBUG
)

# create constants
EXCEL_PATH = os.getcwd() + '/output/financial-statement/{}/{}/'.format(YEAR, AUDITED)
OUTPUT_PATH = os.getcwd() + '/output/dataframe/'
if not os.path.exists(OUTPUT_PATH): os.makedirs(OUTPUT_PATH)

def get_file():
    "Get all Excel files in the given directory."

    # store file names into a list
    f = [x for x in os.listdir(EXCEL_PATH.format(YEAR)) if x.endswith('.xlsx')]

    return f

def create_dataframe(f):
    "Create dataframe for each Excel file."

    df = pd.read_excel(EXCEL_PATH + f, sheet_name = SHEET_INT)

    # store column names and row values as lists
    # put them into a key-value dictionary
    # create dataframe
    col = list(df.iloc[:,COL_INDEX])
    row = list(df.iloc[:,ROW_INDEX])
    d = dict({})
    d.update({'id': f})
    if len(col) == len(row):
        l = len(col)
        for _ in range(l):
            d.update({col[_]: row[_]})
    df = pd.DataFrame([d])

    return df

if __name__ == "__main__":

    # create multiple dataframes simultaneously and save into .csv format
    dfs = multiprocessing.Pool(NUM_POOL).map(create_dataframe, get_file())
    df = pd.concat(dfs, sort=True)\
        .to_csv(OUTPUT_PATH + '{}-{}-{}.csv'\
        .format(DOC_TYPE, YEAR, AUDITED), index=False)