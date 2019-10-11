from json import dump
from requests import get
from os import getcwd
from sys import argv
from time import sleep

OUTPUT_PATH = getcwd() + '/output/'
BASE_URL = 'https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s'
NUM_RETRY = int(argv[1])
SLEEP_TIME = int(argv[2])

def get_emiten():
    "Returns publicly listed companies in Indonesia Stock Exchange."

    i = 0
    while i < NUM_RETRY:
        try:
            response = get(BASE_URL).json()
            with open(OUTPUT_PATH + 'get-companies.json', 'w') as json_file:
                dump(response, json_file)
            i = NUM_RETRY
        except Exception:
            sleep(SLEEP_TIME)
            i += 1
        
if __name__ == "__main__":
    get_emiten()