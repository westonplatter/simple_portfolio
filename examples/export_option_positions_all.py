from simple_portfolio import fetch, export
import configparser

#
# create account dictionary
#
config = configparser.ConfigParser()
config.read('config.debug.ini')
account = dict(
    username = config['account']['username'],
    password = config['account']['password']
)

#
# fetch open options, and only return the open positions
#
fetch_options = { "only_open": False }
positions = fetch.option_positions(account, fetch_options)
print("Fetched {} positions".format(len(positions)))


#
# export to csv
#
fn = "option_positions_all.csv"
export_options = dict(filename = fn)
export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))
