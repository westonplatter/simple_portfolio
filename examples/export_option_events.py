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
events = fetch.option_events(client, fetch_options)
print("Fetched {} option_events".format(len(events)))


fn = "option_events.csv"
export_options = { "filename": fn }

export.option_events(events, export_options)
print("Finished writing option_events to {}".format(fn))
