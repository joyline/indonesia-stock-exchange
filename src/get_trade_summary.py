# load modules
import logging
from json import dump, load
from requests import get
from datetime import date, datetime, timedelta
from multiprocessing import Pool, cpu_count
from os import getcwd
from sys import argv
from string import punctuation
from time import sleep

# log
logfile = date.today().strftime('%Y%m%d')
logging.basicConfig(
    format='%(asctime)s: %(message)s', 
    filename=getcwd() + '/logs/{}.log'.format(logfile), 
    level=logging.DEBUG
)

# create constants
OUTPUT_PATH = getcwd() + '/output/'
BASE_URL = 'https://idx.co.id/umbraco/Surface/TradingSummary/GetStockSummary?date={}&start=0&length={}'

# create arguments
BASE_DATE = argv[1]
NUM_POOL = cpu_count() - int(argv[2])
NUM_RETRY = int(argv[3])
SLEEP_TIME = int(argv[4])
NUM_TIMEOUT = int(argv[5])

def get_urls():
    "Returns URLs that will be crawled to get daily trading summary.s"
    
    # open json file which contains publicly listed companies in IDX
    with open(OUTPUT_PATH + 'get-companies.json', 'r') as json_file:
        data = load(json_file)

    # declare base date
    base_date = datetime.strptime(BASE_DATE, '%Y%m%d').date()
    
    # store URLs for each date
    urls = []
    while base_date <= date.today():
        urls.append(BASE_URL.format(base_date.strftime('%Y%m%d'), len(data)))
        base_date += timedelta(days = 1)

    return urls

def get_trade_summary(urls):
    "Crawls daily trading summary."

    # output file name
    file_name =  urls.translate(str.maketrans('', '', punctuation))

    # attempt three times in case of connection timed out
    # assign time interval betwen attempts
    # save output in json format
    i = 0
    while i < NUM_RETRY:
        try:
            response = get(urls, timeout = NUM_TIMEOUT)
            if response.status_code == 200:
                with open(OUTPUT_PATH + 'trade-summary/' + file_name + '.json', 'w') as json_file:
                    dump(response.json(), json_file)
            i = NUM_RETRY
        except Exception:
            sleep(SLEEP_TIME)
            i += 1

if __name__ == "__main__":
    
    # crawls multiple URLs at the same time
    Pool(NUM_POOL).map(get_trade_summary, get_urls())