# simple metrics for Robinhood
Simple, humble, and direct metrics applied to RH trades

<hr>
# THIS IS IN ALPHA DEVELOPMENT. USE AT YOUR OWN RISK.

<hr>
<hr>
<hr>

## local development

Git clone this repo and run `pip install . --process-dependency-links --editable`



## configs

in an `account.ini` file, provide username and password

```
['account']
username = my_username
password = my_password
```

## commands

export

    ```bash
    sm export_history --trades option
    ```
