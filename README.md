# simple_metrics for Robinhood
Simple portfolio metrics applied to your Robinhood portfolio.

## example

```py
from simple_metrics import fetch, export

account = {
        'username': 'my username',
        'password': 'my password'}

#
# export stock trades to -> stock_orders.csv
#
stock_orders = fetch.stock_trades(account, {})
export.stock_orders(stock_orders, {})

#
# export -> option_orders.csv
#
option_orders = fetch.option_orders(account, {})
export.option_orders(option_orders, {})
```

## install
```sh
pip install simple_metrics --process-dependency-links
```

The package uses a forked version of
[Robinhood](https://github.com/Jamonek/Robinhood), hence
the need for  `--process-dependency-links`.

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

```bash
# stocks
sm export_history --trades stock
# options
sm export_history --trades option
```

## local development
Git clone this repo and run,
```bash
pip install . --process-dependency-links --editable
```

Adding `--editable` allows you to pull in code changes without
having to run `pip install`.
