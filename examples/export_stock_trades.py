from simple_portfolio import fetch, export
import configparser
from fast_arrow import Client


#
# initialize fast_arrow client and authenticate
#
config = configparser.ConfigParser()
config.read('config.debug.ini')
u = config['account']['username']
p = config['account']['password']
client = Client(username = u, password = p)
client.authenticate()


fetch_options = {}
stock_orders = fetch.stock_orders(client, fetch_options)
print("Fetched {} stock trades".format(len(stock_orders)))


fn = "stock_orders.csv"
export_options = {"filename": fn }

export.stock_orders(stock_orders, export_options)
print("Finished writing stock_orders to {}".format(fn))
