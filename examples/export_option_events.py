from simple_portfolio import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')


account = {
        'username': config['account']['username'],
        'password': config['account']['password']}


fetch_options = {}
events = fetch.option_events(account, fetch_options)
print("Fetched {} option_events".format(len(events)))


fn = "option_events.csv"
export_options = { "filename": fn }

export.option_events(events, export_options)
print("Finished writing option_events to {}".format(fn))
