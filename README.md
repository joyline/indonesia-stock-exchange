# indonesia-stock-exchange

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free (one of the things you could do especiallly when you're not rich AF) :stuck_out_tongue_closed_eyes:. It includes both technical and fundamental information, such as stock prices (opening, closing, bid, ask, volume, etc) and financial statements (balance sheet, profit and loss, changes in equity, cash flow). Surely the information contained is more diverse than we can find from other free source (e.g. Yahoo! Finance) and far cheaper than using financial terminal (e.g. Bloomberg). 

I have only tested this using Python 3.7.3 (:snake:), but it should be fine for any Python 3.x. However, I won't bother testing it using Python 2.x. You can read [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for more details. Or you can visit [my Medium](https://medium.com/@lukmanedwindra/get-financial-information-from-indonesian-publicly-listed-companies-for-free-74870235f783) article related to this repository. I hope this can be useful for your own purpose. :smile:

## Install Requirements

Run the following in the terminal :computer::

```
pip install -r requirements.txt
```

## Add this Repo to Your Machine

Run the following in the terminal :computer::

```
git clone https://github.com/ledwindra/indonesia-stock-exchange.git
```

## Example

### Daily Trading Summary

Following is the template :snake::
```
python src/get_trading_summary.py [BASE_DATE] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```

Following is the example :snake::

```
python src/get_trading_summary.py 20191104 1 3 30 10
```

See [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for details.

### Financial Statements

Following is the template :snake::

```
python src/get_financial_statement.py [YEAR] [AUDITED] [YEARLY] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```

Following is the example :snake::

```
python src/get_financial_statement.py 2018 Audit Tahunan 1 3 30 10
```

See [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for details.

## Shell :shell:

To ease your mind, run those Python programs simultaneously using your terminal :computer::

```
sh ./bash/financial-statement.sh [YEAR] [NUM_POOL] [NUM_RETRY] [SLEEP_TIME] [NUM_TIMEOUT]
```

And the following:

```
financial-statement-dataframe.sh [BEG_YEAR] [END_YEAR]
```

## End
Hope you enjoy this. Once again, see [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for details. Thanks for reading! :smile:
