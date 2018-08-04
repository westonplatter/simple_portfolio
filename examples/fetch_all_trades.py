from simple_metrics import fetch
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')

account = {
        'username': config['account']['username'],
        'password': config['account']['password']}

fetch_options = {}

orders = fetch.stock_orders(account, fetch_options)
msg = "Fetched {} stock trades".format(len(orders))
print(msg)

option_orders = fetch.option_orders(account, fetch_options)
msg = "Fetched {} option trades".format(len(option_orders))
print(msg)
