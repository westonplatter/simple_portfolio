# error in RH
import dateutil

from Robinhood import Robinhood


def fetch_json_by_url(client, url):
    return client.session.get(url).json()


def stock_trades(account, options={}):
    client = Robinhood()
    client.login(username=account['username'], password=account['password'])

    orders = []
    more_orders = True

    res = client.order_history()
    orders.extend(res['results'])
    cursor = res['next']
    while cursor:
        res = fetch_json_by_url(client, cursor)
        orders.extend(res['results'])
        cursor = res['next']

    return orders


def option_orders(account, options={}):
    client = Robinhood()
    client.login(username=account['username'], password=account['password'])

    options_orders = []
    more_orders = True

    res = client.options_order_history()
    options_orders.extend(res['results'])
    cursor = res['next']

    while cursor:
        res = fetch_json_by_url(client, cursor)
        options_orders.extend(res['results'])
        cursor = res['next']

    return options_orders
