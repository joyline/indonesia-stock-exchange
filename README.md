# indonesia-stock-exchange

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free. It includes both technical and fundamental information, such as stock prices (opening, closing, bid, ask, volume, etc) and financial statements (balance sheet, profit and loss, changes in equity, cash flow). Surely the information contained is more diverse than we can find from other free source (e.g. Yahoo! Finance) and far cheaper than using financial terminal (e.g. Bloomberg). 

I have only tested this using Python 3.7.3, but it should be fine for any Python 3.x. However, I won't bother testing it using Python 2.x. You can read [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki) for more details. Or you can visit [my Medium](https://medium.com/@lukmanedwindra/get-financial-information-from-indonesian-publicly-listed-companies-for-free-74870235f783) article related to this repository. I hope this can be useful for your own purpose. :)

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

Following is the template:
```
python src/get_trading_summary.py [BASE_DATE] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```

Following is the example:

```
python src/get_trading_summary.py 20191104 1 3 30 10
```

See [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki) for details.

### Financial Statements

Following is the template:

```
python src/get_financial_statement.py [YEAR] [AUDITED] [YEARLY] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```

Following is the example:

```
python src/get_financial_statement.py 2018 Audit Tahunan 1 3 30 10
```

See [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki) for details.
