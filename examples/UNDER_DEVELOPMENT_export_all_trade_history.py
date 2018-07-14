import simple_metrics as sm

import configparser

config = configparser.ConfigParser()

username = config['username']
password = config['password']

account = {
        'username': username,
        'password': password}

options = {
        'duration': '3m'}

sm.export_stock_trades(account, options)
sm.export_option_trades(account, options)
