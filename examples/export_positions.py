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
positions = fetch.positions(client, fetch_options)
print("Fetched {} positions".format(len(positions)))

fn = "positions.csv"
export_options = { "filename": fn }

export.positions(positions, export_options)
print("Finished writing positions to {}".format(fn)
