from simple_metrics import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = {}
positions = fetch.positions(account, fetch_options)
print("Fetched {} positions".format(len(positions)))

fn = "positions.csv"
export_options = { "filename": fn }

export.positions(positions, export_options)
print("Finished writing positions to {}".format(fn)
