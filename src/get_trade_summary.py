from json import dump, load
from requests import get
from datetime import date, datetime, timedelta
from multiprocessing import Pool, cpu_count
from os import getcwd
from sys import argv
from string import punctuation
from time import sleep

OUTPUT_PATH = getcwd() + '/output/'
BASE_URL = 'https://idx.co.id/umbraco/Surface/TradingSummary/GetStockSummary?date={}&start=0&length={}'
BASE_DATE = argv[1]
NUM_POOL = cpu_count() - int(argv[2])
NUM_RETRY = int(argv[3])
SLEEP_TIME = int(argv[4])
NUM_TIMEOUT = int(argv[5])

def get_trade_summary():
    
    with open(OUTPUT_PATH + 'get-companies.json', 'r') as json_file:
        data = load(json_file)

    base_date = datetime.strptime(BASE_DATE, '%Y%m%d').date()
    
    urls = []
    while base_date <= date.today():
        urls.append(BASE_URL.format(base_date.strftime('%Y%m%d'), len(data)))
        base_date += timedelta(days = 1)

    return urls

def main(urls):

    file_name =  urls.translate(str.maketrans('', '', punctuation))
    response = get(urls, timeout = NUM_TIMEOUT)
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
    
    Pool(NUM_POOL).map(main, get_trade_summary())
