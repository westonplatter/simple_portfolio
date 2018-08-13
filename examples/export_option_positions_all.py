from simple_metrics import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = { "only_open": False }
positions = fetch.option_positions(account, fetch_options)
print("Fetched {} positions".format(len(positions)))


fn = "option_positions_all.csv"
export_options = { "filename": fn }
export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))
