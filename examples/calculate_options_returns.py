from simple_portfolio import (calculate, fetch, export)
import configparser
from fast_arrow import (Client, OptionOrder)


config = configparser.ConfigParser()
config.read('config.debug.ini')


#
# initialize fast_arrow client and authenticate
#
client = Client(
    username = config['account']['username'],
    password = config['account']['password'])

client.authenticate()


#
# fetch option orders
#
fetch_options = { "only_filed": True }
option_orders_raw = fetch.option_orders(client, fetch_options)
option_orders = OptionOrder.unroll_option_legs(client, option_orders_raw)

print("Fetched {} option orders".format(len(option_orders)))
fn = "option_orders.csv"
export_options = dict(filename = fn)
export.option_orders(option_orders, export_options)
print("Finished writing option_orders to {}".format(fn))


#
# option events
#
fetch_options = {}
events = fetch.option_events(client, fetch_options)
print("Fetched {} option_events".format(len(events)))
fn = "option_events.csv"
export_options = dict(filename = fn)
export.option_events(events, export_options)
print("Finished writing option_events to {}".format(fn))


#
# fetch option positions
#
fetch_options = dict()
positions = fetch.option_positions(client, fetch_options)
print("Fetched {} positions".format(len(positions)))

fn = "option_positions.csv"
export_options = dict(filename = fn)
export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))

df = calculate.doit()
print(df)
