from Robinhood import Robinhood
import fast_arrow


def fetch_json_by_url(client, url):
    return client.session.get(url).json()


def stock_orders(account, options={}):
    client = _get_client(account)

    stock_orders = []
    more_orders = True

    res = client.order_history()
    stock_orders.extend(res['results'])
    cursor = res['next']
    while cursor:
        res = fetch_json_by_url(client, cursor)
        stock_orders.extend(res['results'])
        cursor = res['next']

    return stock_orders


def option_orders(account, options={}):
    client = _get_client(account)

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


def positions(account, options={}):
    client = _get_client(account)

    positions = []

    res = client.positions()
    positions.extend(res['results'])
    cursor = res['next']
    while cursor:
        res = fetch_json_by_url(client, cursor)
        positions.extend(res['results'])
        cursor = res['next']

    for index,x in enumerate(positions):
        data = fetch_json_by_url(client, x['instrument'])
        positions[index]['instrument_data'] = data

    return positions

def option_positions(account, options={}):
    """
    use fast_arrow to fetch positions
    """
    username = account["username"]
    password = account["password"]
    from fast_arrow.resources.auth import Auth
    token = Auth.login(username, password)

    from fast_arrow.resources.option_position import OptionPosition
    all_option_positions = OptionPosition.all(token)
    open_option_positions = list(filter(lambda p: float(p["quantity"]) > 0.0, all_option_positions))

    bearer = Auth.get_oauth_token(token)
    results = OptionPosition.append_marketdata(bearer, open_option_positions)

    return results


def _get_client(account):
    client = Robinhood()
    client.login(username=account['username'], password=account['password'])
    return client
