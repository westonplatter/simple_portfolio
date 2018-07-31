import csv
from . import fetch

def option_orders(option_orders, options = {}):
    drows = option_orders
    cols = [*drows[0].keys()]
    headers = order_option_cols(cols)
    filename = "option_orders.csv"

    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            [writer.writerow(drow) for drow in drows]
    except IOError:
        print("I/O error")


def stock_orders(stock_orders, options = {}):
    drows = stock_orders
    cols = [*drows[0].keys()]
    headers = ordered_stock_cols(cols)
    filename = "stock_orders.csv"

    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            [writer.writerow(drow) for drow in drows]
    except IOError:
        print("I/O Error")


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


def ordered_stock_cols(cols):
    expected_headers_ordered = [
        'id', 'ref_id', 'instrument', 'updated_at', 'created_at', 'last_transaction_at',
        'time_in_force', 'trigger', 'cancel', 'response_category','state', 'reject_reason',
        'type', 'side', 'price', 'stop_price', 'average_price', 'quantity', 'cumulative_quantity', 'fees',
        'executions', 'extended_hours', 'account', 'url', 'position',
        'override_day_trade_checks', 'override_dtbp_checks',
    ]

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


def _write_file(filename, headers, rows):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            [writer.writerow(row) for row in rows]
    except IOError:
        print("I/O Error")
