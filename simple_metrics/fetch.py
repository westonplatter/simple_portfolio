from fast_arrow import (
    Auth,
    StockOrder,
    StockPosition,
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
    if ("only_filled" in options) and options["only_filled"]:
        orders = list(filter(lambda x: x["state"] == "filled", orders))
    return orders


def positions(account, options={}):
    token = _get_token(account["username"], account["password"])
    ps = StockPosition.all(token)
    if ("only_open" in options) and options["only_open"]:
        ps = list(filter(lambda x: float(x["quantity"]) > 0.0, ps))
    return ps


def option_positions(account, options={}):
    token = _get_token(account["username"], account["password"])
    all_option_positions = OptionPosition.all(token)
    open_option_positions = list(filter(lambda p: float(p["quantity"]) > 0.0, all_option_positions))
    bearer = _get_bearer(token)
    results = OptionPosition.append_marketdata(bearer, open_option_positions)
    return results




def _get_token(username, password):
    token = Auth.login(username, password)
    return token


def _get_bearer(token):
    bearer = Auth.get_oauth_token(token)
    return bearer
