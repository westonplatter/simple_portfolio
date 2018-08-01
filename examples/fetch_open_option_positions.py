from simple_metrics import fetch
import configparser
import pprint

config = configparser.ConfigParser()
config.read('config.debug.ini')

account = {
        'username': config['account']['username'],
        'password': config['account']['password']}

fetch_options = {}
option_positions = fetch.option_positions(account, fetch_options)

msg = "Fetched {} open option positions".format(len(positions))
pprint.pprint(msg)

pprint.pprint("First option position in array ...\n\n\n")
pprint.pprint(option_positions[0])
