import csv


def option_orders(option_orders, options = {}):
    drows = option_orders
    cols = [*drows[0].keys()]
    headers = order_option_cols(cols)
    fn = _get_config_or_default(options, "filename", "option_orders.csv")
    _write_file_get_header_values(fn, headers, drows)


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
    fn = _get_config_or_default(options, "filename", "stock_orders.csv")
    _write_file_get_header_values(fn, headers, drows)


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
    drows = positions
    cols = list(drows[0].keys())
    headers = cols
    fn = _get_config_or_default(options, "filename", "stock_positions.csv")
    _write_file_get_header_values(fn, headers, drows)


def option_positions(drows, options={}):
    fn = _get_config_or_default(options, "filename", "option_positions.csv")
    headers = expected_option_position_fields()
    _write_file_get_header_values(fn, headers, drows)


def expected_option_position_fields():
    return [
        'id', 'chain_symbol', 'type', 'option_type', 'strike_price',
        'expiration_date', 'quantity', 'average_price',

        'adjusted_mark_price', 'ask_price', 'ask_size', 'bid_price',
        'bid_size',
        'mark_price', 'low_price', 'high_price',
        'last_trade_price', 'last_trade_size',
        'previous_close_date', 'previous_close_price',

        'open_interest', 'volume', 'chance_of_profit',
        'implied_volatility', 'delta', 'theta', 'gamma', 'rho', 'vega',

        'intraday_average_open_price', 'account', 'intraday_quantity',
        'option', 'created_at', 'updated_at', 'chain_id',
        'pending_expired_quantity', 'pending_buy_quantity', 'url',
        'pending_sell_quantity', 'break_even_price',  'instrument'
    ]


def option_events(drows, export_options={}):
    fn = _get_config_or_default(export_options, "filename", "option_events.csv")
    headers = expected_option_event_fields()
    _write_file_get_header_values(fn, headers, drows)

def expected_option_event_fields():
    return [
        'id', 'option','chain_id', 'state', 'type', 'direction', 'quantity', 'equity_components', 'position',
        'updated_at', 'created_at',   'underlying_price', 'cash_component', 'event_date',  'total_cash_amount', 'account'
    ]

def _write_file_get_header_values(filename, headers, rows):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in rows:
                row_to_write = dict((k, row[k]) for k in headers if k in row)
                writer.writerow(row_to_write)
    except IOError:
        print("I/O Error")


def _get_config_or_default(options, key, default):
    if key in options:
        return options[key]
    else:
        return default
