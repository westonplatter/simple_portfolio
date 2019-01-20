from fast_arrow import (
    Client,
    Option,
    OptionEvent,
    OptionPosition,
    OptionOrder,
    StockOrder,
    StockPosition,
)
from fast_arrow import util as fa_util
from simple_portfolio import util


def stock_orders(client, options={}):
    '''
    options:
        - only_filled. Only return filled orders. Default = False.
    '''
    orders = StockOrder.all(client)
    only_filled = util.get_key(options, "only_filled", True)
    if only_filled:
        orders = list(filter(lambda x: x["state"] == "filled", orders))
    return orders


def option_orders(client, options={}):
    '''
    options:
        - only_filled. Default = True
    '''
    x = OptionOrder.all(client)
    only_filled = util.get_key(options, "only_filled", True)
    if only_filled:
        x = list(filter(lambda j: j["state"] == "filled", x))
    x = OptionOrder.humanize_numbers(x)
    return x


def stock_positions(client, options={}):
    return StockPosition.all(client)


def option_positions(client, options={}):
    '''
    options:
        - only_open. Default = True
    '''
    x = OptionPosition.all(client)
    only_open = util.get_key(options, "only_open", True)
    if only_open:
        x = list(filter(lambda p: float(p["quantity"]) > 0.0, x))
        x = OptionPosition.mergein_marketdata_list(client, x)
        x = OptionPosition.mergein_instrumentdata_list(client, x)
        x = OptionPosition.humanize_numbers(x)
    return x


def option_events(client, options={}):
    '''
    options:
    '''
    x = OptionEvent.all(client)
    x = OptionEvent.mergein_instrumentdata_list(client, x)
    x = OptionEvent.humanize_numbers(x)
    return x
