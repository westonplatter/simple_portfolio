import csv
from . import fetch

def stock_trades(account, options):
    stock_orders = fetch.stock_trades(account, options)
    write_rows_of_dictionaries()

    print('exporting RH stock history')

def option_orders(option_orders, options = {}):
    drows = option_orders
    cols = [*drows[0].keys()]
    filename = "option_orders.csv"

    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cols)
            writer.writeheader()
            for drow in drows:
                writer.writerow(drow)
    except IOError:
        print("I/O error")
