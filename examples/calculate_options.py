from simple_portfolio import calculate, fetch, export
import configparser
from fast_arrow import OptionOrder

config = configparser.ConfigParser()
config.read('config.debug.ini')

#
# pull username and password from "simple_portfolio/config.debug.ini"
#
account = {
        'username': config['account']['username'],
        'password': config['account']['password']}

#
# fetch option orders
#
fetch_options = {}
option_orders = fetch.option_orders(account, fetch_options)
print("Fetched {} option orders".format(len(option_orders)))
fn = "option_orders.csv"
export_options = { "filename": fn }
export.option_orders(option_orders, export_options)
print("Finished writing option_orders to {}".format(fn))


#
# option events
#
fetch_options = {}
events = fetch.option_events(account, fetch_options)
print("Fetched {} option_events".format(len(events)))
fn = "option_events.csv"
export_options = { "filename": fn }
export.option_events(events, export_options)
print("Finished writing option_events to {}".format(fn))

#
# fetch option positions
#
fetch_options = {}
positions = fetch.option_positions(account, fetch_options)
print("Fetched {} positions".format(len(positions)))

fn = "option_positions.csv"
export_options = { "filename": fn }
export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))

df = calculate.doit()
print(df)
