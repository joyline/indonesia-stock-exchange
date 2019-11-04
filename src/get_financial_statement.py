import json
import logging
import multiprocessing
import os
import requests
import string
import sys
from datetime import date
from time import sleep

# create arguments
YEAR = sys.argv[1]
AUDITED = sys.argv[2]
YEARLY = sys.argv[3]
NUM_POOL = multiprocessing.cpu_count() - int(sys.argv[4])
NUM_RETRY = int(sys.argv[5])
SLEEP_TIME = int(sys.argv[6])
NUM_TIMEOUT = int(sys.argv[7])

# log
logfile = date.today().strftime('%Y%m%d')
logging.basicConfig(
    format='%(asctime)s: %(message)s', 
    filename=os.getcwd() + '/logs/financial-statement-{}-{}.log'.format(YEAR, AUDITED.lower()), 
    level=logging.DEBUG
)

# create constants
OUTPUT_PATH = os.getcwd() + '/output/financial-statement/{}/'.format(YEAR)
if not os.path.exists(OUTPUT_PATH): os.mkdir(OUTPUT_PATH)
BASE_URL = 'http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%20{0}/{1}/{2}/FinancialStatement-{0}-{3}-{2}.xlsx'

def get_urls():
    
    # open json file which contains publicly listed companies in IDX
    with open(os.getcwd() + '/output/get-companies.json', 'r') as json_file:
        data = json.load(json_file)

    ticker = [list(x.values())[0] for x in data]
    urls = [BASE_URL.format(YEAR, AUDITED, x, YEARLY) for x in ticker]

    return urls

def get_financial_statement(urls):

    file_name = urls.replace('http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%20', '')
    file_name =  file_name.translate(str.maketrans('', '', string.punctuation))
    i = 0
    while i < NUM_RETRY:
        try:
            response = requests.get(urls, timeout=NUM_TIMEOUT)
            if response.status_code == 200:
                with open(OUTPUT_PATH + file_name + '.xlsx', 'wb') as f:
                    f.write(response.content)
            i = NUM_RETRY
        except Exception as e:
            logging.error('{}: '.format(urls) + e)
            sleep(SLEEP_TIME)
            i += 1

if __name__ == "__main__":
    multiprocessing.Pool(NUM_POOL).map(get_financial_statement, get_urls())