from simple_portfolio import fetch
import configparser
import pprint
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
stock_positions = fetch.positions(client, fetch_options)

msg = "Fetched {} stock positions".format(len(stock_positions))
pprint.pprint(msg)

pprint.pprint("First position in array ...\n\n\n")
pprint.pprint(stock_positions[0])
