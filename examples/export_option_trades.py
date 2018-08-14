from simple_portfolio import fetch, export
from fast_arrow import OptionOrder
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = {}
option_orders = fetch.option_orders(account, fetch_options)
print("Fetched {} option trades".format(len(option_orders)))

# humanize_numbers
option_orders = OptionOrder.humanize_numbers(option_orders)

fn = "option_orders.csv"
export_options = { "filename": fn }
export.option_orders(option_orders, export_options)
print("Finished writing option_orders to {}".format(fn))
