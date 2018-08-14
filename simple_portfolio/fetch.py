from fast_arrow import (
    Auth,
    StockOrder,
    StockPosition,
    OptionEvent,
    OptionPosition,
    OptionOrder
)


def stock_orders(account, options={}):
    token = _get_token(account["username"], account["password"])
    orders = StockOrder.all(token)
    if ("only_filled" in options) and options["only_filled"]:
        orders = list(filter(lambda x: x["state"] == "filled", orders))
    return orders


def option_orders(account, options={}):
    token = _get_token(account["username"], account["password"])
    orders = OptionOrder.all(token)
    return orders


def positions(account, options={}):
    token = _get_token(account["username"], account["password"])
    ps = StockPosition.all(token)
    return ps


def option_positions(account, options={}):
    only_open = _get_config_or_default(options, "only_open", True)

    token = _get_token(account["username"], account["password"])
    bearer = _get_bearer(token)

    ops = OptionPosition.all(bearer)

    if not only_open:
        return ops
    else:
        ops = list(filter(lambda p: float(p["quantity"]) > 0.0, ops))
        ops = OptionPosition.mergein_marketdata_list(bearer, ops)
        ops = OptionPosition.mergein_instrumentdata_list(bearer, ops)
        ops = OptionPosition.humanize_numbers(ops)
        return ops


def option_events(account, fetch_options={}):
    token = _get_token(account["username"], account["password"])
    bearer = _get_bearer(token)
    option_events = OptionEvent.all(bearer)

    for oe in option_events:
        if len(oe["equity_components"]) > 0:
            oe['symbol'] = oe["equity_components"][0]["symbol"]
            
    return option_events


def _get_token(username, password):
    token = Auth.login(username, password)
    return token


def _get_bearer(token):
    bearer = Auth.get_oauth_token(token)
    return bearer

def _get_config_or_default(options, key, default):
    if key in options:
        return options[key]
    else:
        return default
