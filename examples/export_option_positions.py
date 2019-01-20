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
# fetch positions
#
fopts = {}
positions = fetch.option_positions(client, fopts)
print("Fetched {} positions".format(len(positions)))


#
# export positions
#
fn = "option_positions.csv"
eopts = {"filename": fn}
export.option_positions(positions, opts)
print("Finished writing positions to {}".format(fn))
