from simple_metrics import fetch
import configparser
import pprint

config = configparser.ConfigParser()
config.read('config.debug.ini')

account = {
        'username': config['account']['username'],
        'password': config['account']['password']}

fetch_options = {}
positions = fetch.positions(account, fetch_options)

msg = "Fetched {} stock trades".format(len(positions))
pprint.pprint(msg)

pprint.pprint("First position in array ...\n\n\n")
pprint.pprint(positions[0])
