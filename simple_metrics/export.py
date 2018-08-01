import csv
from . import fetch

def option_orders(option_orders, options = {}):
    drows = option_orders
    cols = [*drows[0].keys()]
    headers = order_option_cols(cols)
    filename = "option_orders.csv"
    _write_file(filename, headers, drows)


def order_option_cols(cols):
    expected_headers_ordered = [
        "id", "chain_id", "ref_id",  "updated_at", "created_at", "time_in_force",
        "chain_symbol", "state", "type", "direction", "price", "premium", "processed_premium",
        "quantity", "pending_quantity", "processed_quantity",
        "opening_strategy", "closing_strategy", "legs",
        "trigger", "response_category",
        "cancel_url", "canceled_quantity",
    ]

    if set(cols) == set(expected_headers_ordered):
        return expected_headers_ordered
    else:
        return cols


def stock_orders(stock_orders, options = {}):
    drows = stock_orders
    cols = [*drows[0].keys()]
    headers = ordered_stock_cols(cols)
    filename = "stock_orders.csv"
    _write_file(filename, headers, drows)


def ordered_stock_cols(cols):
    expected_headers_ordered = [
        'id', 'ref_id', 'instrument', 'updated_at', 'created_at', 'last_transaction_at',
        'time_in_force', 'trigger', 'cancel', 'response_category','state', 'reject_reason',
        'type', 'side', 'price', 'stop_price', 'average_price', 'quantity', 'cumulative_quantity', 'fees',
        'executions', 'extended_hours', 'account', 'url', 'position',
        'override_day_trade_checks', 'override_dtbp_checks']

    if set(cols) == set(expected_headers_ordered):
        return expected_headers_ordered
    else:
        return cols


def positions(positions, options = {}):
    rows = positions
    cols = [*rows[0].keys()]
    headers = cols
    filename = "all_positions.csv"
    _write_file(filename, headers, rows)


def option_positions(drows, options={}):
    filename = "option_positions.csv"
    cols = list(drows[0].keys())
    headers = ordered_option_position_cols(cols)
    _write_file(filename, headers, drows)


def ordered_option_position_cols(cols):
    expected_headers_ordered = [
        'id', 'chain_symbol', 'type', 'quantity',

        'adjusted_mark_price', 'ask_price', 'ask_size', 'bid_price', 'bid_size',
        'high_price',
        'last_trade_price', 'last_trade_size', 'low_price', 'mark_price',
        'open_interest', 'previous_close_date', 'previous_close_price',
        'volume', 'chance_of_profit_long', 'chance_of_profit_short', 'delta',
        'gamma', 'implied_volatility', 'rho', 'theta', 'vega',

        'intraday_average_open_price', 'account', 'intraday_quantity', 'option', 'created_at', 'updated_at', 'average_price', 'chain_id', 'pending_expired_quantity', 'pending_buy_quantity', 'url', 'pending_sell_quantity', 'break_even_price',  'instrument'
    ]

    if set(cols) == set(expected_headers_ordered):
        return expected_headers_ordered
    else:
        return cols


def _write_file(filename, headers, rows):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            [writer.writerow(row) for row in rows]
    except IOError:
        print("I/O Error")
