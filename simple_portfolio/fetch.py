from fast_arrow import (
    Client,
    StockOrder, StockPosition,
    OptionEvent, OptionPosition, OptionOrder, Option
)
from simple_portfolio import util


def stock_orders(account, options={}):
    '''
    options:
        - only_filled. Only return filled orders. Default = False.
    '''
    client = _init_client(account["username"], account["password"])
    orders = StockOrder.all(client)
    only_filled = util.get_key(options, "only_filled", True)
    if only_filled:
        orders = list(filter(lambda x: x["state"] == "filled", orders))
    return orders


def option_orders(account, options={}):
    '''
    options:
        - only_filled:
    '''
    client = _init_client(account["username"], account["password"])
    x = OptionOrder.all(client)
    only_filled = util.get_key(options, "only_filled", True)
    if only_filled:
        x = list(filter(lambda j: j["state"] == "filled", x))
    x = OptionOrder.humanize_numbers(x)
    return x

def stock_positions(account, options={}):
    '''
    options:
    '''
    client = _init_client(account["username"], account["password"])
    x = StockPosition.all(client)
    return x


def option_positions(account, options={}):
    '''
    options:
        - only_open. Default = True
    '''
    client = _init_client(account["username"], account["password"])
    x = OptionPosition.all(client)
    only_open = util.get_key(options, "only_open", True)
    if only_open:
        x = list(filter(lambda p: float(p["quantity"]) > 0.0, x))
        x = OptionPosition.mergein_marketdata_list(client, x)
        x = OptionPosition.mergein_instrumentdata_list(client, x)
        x = OptionPosition.humanize_numbers(x)
    return x

def option_events(account, options={}):
    '''
    options:
    '''
    client = _init_client(account["username"], account["password"])
    x = OptionEvent.all(client)
    x = OptionEvent.mergein_instrumentdata_list(client, x)
    x = OptionEvent.humanize_numbers(x)
    return x


def _init_client(username, password):
    client = Client(username=username, password=password)
    client.authenticate()
    return client
