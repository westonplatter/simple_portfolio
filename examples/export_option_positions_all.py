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


#
# fetch open options, and only return the open positions
#
fetch_options = { "only_open": False }
positions = fetch.option_positions(client, fetch_options)
print("Fetched {} positions".format(len(positions)))


#
# export to csv
#
fn = "option_positions_all.csv"
export_options = dict(filename = fn)
export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))
