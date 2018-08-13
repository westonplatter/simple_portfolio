from simple_metrics import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = {}
stock_orders = fetch.stock_orders(account, fetch_options)
print("Fetched {} stock trades".format(len(stock_orders)))


fn = "stock_orders.csv"
export_options = {"filename": fn }

export.stock_orders(stock_orders, export_options)
print("Finished writing stock_orders to {}".format(fn))
