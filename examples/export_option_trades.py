from simple_metrics import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = {}
option_orders = fetch.option_orders(account, fetch_options)
print("Fetched {} option trades".format(len(option_orders)))


export_options = {}
export.option_orders(option_orders, export_options)
print("finished writing option_orders to option_orders.csv")
