# indonesia-stock-exchange

For detais, go to [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki).

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free. This has only been tested using Python 3.7.3, but it should be fine for any Python 3.x. However, I won't bother testing it using Python 2.x

## Install Requirements

Run the following in the terminal:

```
pip install -r requirements.txt
```

## Add this Repo to Your Machine

Run the following in the terminal:

```
git clone https://github.com/ledwindra/indonesia-stock-exchange.git
```

## Example

### Daily Trading Summary

Run the following in the terminal:
```
python src/get_trading_summary.py [BASE_DATE] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```