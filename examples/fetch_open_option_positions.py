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
option_positions = fetch.option_positions(client, fetch_options)

msg = "Fetched {} open option positions".format(len(option_positions))
pprint.pprint(msg)

pprint.pprint("First option position in array ...\n\n\n")
pprint.pprint(option_positions[0])
