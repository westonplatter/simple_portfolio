# simple metrics for Robinhood
Simple, humble, and direct metrics applied to RH trades

<hr>
# THIS IS IN ALPHA DEVELOPMENT. USE AT YOUR OWN RISK.
<hr>

## example

```
from simple_metrics import fetch, export

account = {
        'username': 'my username',
        'password': 'my password'}

stock_orders = fetch.stock_trades(account, {})
export.stock_orders(stock_orders, {})
# exports -> stock_orders.csv

option_orders = fetch.option_orders(account, {})
export.option_orders(option_orders, {})
# exports -> option_orders.csv
```

## package api

Functionality includes:

- Fetch Stock order history
- Fetch Option order history
- Export Stock order history
- Export Option order history


## command line usage

### config

in an `account.ini` file, provide username and password

```
['account']
username = my_username
password = my_password
```

### cli commands

export

    sm export_history --trades stock

    sm export_history --trades option


## local development

Git clone this repo and run `pip install . --process-dependency-links --editable`
