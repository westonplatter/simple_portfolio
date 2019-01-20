from simple_portfolio import fetch, export
import configparser
from fast_arrow import OptionOrder, Client


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
option_orders = fetch.option_orders(client, fetch_options)
print("Fetched {} option trades".format(len(option_orders)))

# humanize_numbers
# option_orders = OptionOrder.humanize_numbers(option_orders)

fn = "option_orders.csv"
export_options = { "filename": fn }
export.option_orders(option_orders, export_options)
print("Finished writing option_orders to {}".format(fn))
