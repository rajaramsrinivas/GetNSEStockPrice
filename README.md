#GetNSEStockPrice
Simple python library that consumes HTTP REST data of sttock prices provided by Google and Yahoo Finance APIs.
Can be used both as a library as well as a command line tool

To receive email alerts in case of failures, use the config file config.py to setup SMTP server credentials.

- Rajaram, May 2016
- License: GPL v2

## Installation
pip / easy_install
```bash
   sudo pip install GetNSEStockPrice
```

##Usage
```python
from GetNSEStockPrice import get_stock
scrips_to_fetch = ['INFY','RELIANCE','TCS','ITC','BAJAJ-AUTO']
stocks =  get_stock.get_stock_price(scrips_to_fetch)
print 'Stock price of Infosys as of %s is %s'%(stocks['INFY']['timestamp'], stocks['INFY']['price'])

```

##From the command line
```bash
python get_stock.py -h
usage: get_stock.py [-h] s

Gets stock prices of scrips listed in NSE

positional arguments:
  s           Comma separated list of scrips by scrip_code in NSE

  optional arguments:
    -h, --help  show this help message and exit

```
To fetch the price of one or more scrips, pass it on as as the first positional argument.
```bash
python get_stock.py TCS,INFY
{u'TCS': {'volume': u'674732', 'timestamp': datetime.datetime(2016, 5, 30, 15, 29, 58, tzinfo=tzfile('/usr/share/zoneinfo/Asia/Kolkata')), 'price': u'2636.399902'}, u'INFY': {'volume': u'2642850', 'timestamp': datetime.datetime(2016, 5, 30, 15, 30, tzinfo=tzfile('/usr/share/zoneinfo/Asia/Kolkata')), 'price': u'1267.599976'}}
```
