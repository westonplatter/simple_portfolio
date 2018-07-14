import click
import functools
from . import export, fetch


def get_username_password(config_file):
    import configparser
    config = configparser.ConfigParser()
    config.read(config_file)

    username = config['account']['username']
    password = config['account']['password']

    account = {
            'username': username,
            'password': password}
    return account


def common_options(func):
    @click.option('--debug/--no-debug', default=False)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@click.group()
def cli():
    pass


@cli.command()
@click.option('--config-file', default="config.ini", required=False)
@click.option('--trades', default="stock",
    type=click.Choice(['stock', 'option']), required=False)
@click.option('--duration', default="1m")
@click.option('--export-file', default="default.csv", required=False)
@common_options
def export_history(debug, duration, config_file, trades, export_file):
    if debug and config_file == "config.ini":
        config_file = "config.debug.ini"
    account = get_username_password(config_file)

    if trades == 'stock':
        # export.stock_trades(account, export_file)
        raise("still under development")
    elif trades == 'option':
        fetch_options = {}
        option_orders = fetch.option_orders(account, fetch_options)
        export_options = {}
        export.option_orders(option_orders, export_options)


if __name__ == '__main__':
    cli()
