
def get_key(options, k, default):
    if k in options:
        return options[k]
    else:
        return default
