import csv
from . import fetch

def stock_trades(account, options):
    stock_orders = fetch.stock_trades(account, options)
    write_rows_of_dictionaries()

    print('exporting RH stock history')

def option_orders(option_orders, options = {}):
    drows = option_orders
    cols = [*drows[0].keys()]
    headers = order_option_cols(cols)
    filename = "option_orders.csv"

    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for drow in drows:
                writer.writerow(drow)
    except IOError:
        print("I/O error")


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
