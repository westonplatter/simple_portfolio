import pandas as pd
import numpy as np

def doit():
    #
    # option orders
    #
    oos = pd.read_csv("./option_orders.csv")
    oos["symbol"] = oos["chain_symbol"]
    oos = oos[oos.state == "filled"]
    agg_oos = ( oos[["symbol", "price"]].
                    groupby(["symbol"]).
                    agg({
                        "price": {
                            "oo_total": "sum",
                            "oo_count": "count"
                    }}).
                    sort_values(("price", "oo_total"))
                )

    agg_oos.columns = [x[1] for x in agg_oos.columns.ravel()]


    #
    # option events
    #
    oes = pd.read_csv("./option_events.csv")
    exercised_or_assigned_oes = oes[oes.type.str.contains("assignment|exercise", regex=True)]
    agg_oes = ( exercised_or_assigned_oes[["symbol", "total_cash_amount"]].
                    groupby(["symbol"]).
                    agg({
                        "total_cash_amount": {
                            "oe_total": "sum",
                            "oe_count": "count"
                        }
                    }).
                    sort_values(("total_cash_amount", "oe_total")) )

    agg_oes.columns = [x[1] for x in agg_oes.columns.ravel()]


    #
    # option positions
    #
    ops = pd.read_csv("./option_positions.csv")
    ops["symbol"] = ops["chain_symbol"]

    ops["coef"] = np.where(ops["type"] == "long", 1.0, -1.0)

    # calcalate diff between yesterday and today
    ops["market_value"] = ops["quantity"] * ops["adjusted_mark_price"]
    ops["pv_prev"]   = ops["quantity"] * ops["previous_close_price"]
    ops["pv_orig"]   = ops["coef"] * ops["quantity"] * ops["average_price"] / 100.0

    ops["return_today"] = ops["market_value"] - ops["pv_prev"]
    ops["return_total"] = ops["market_value"] - ops["pv_orig"]


    agg_ops = ( ops[["symbol", "market_value", "return_today", "pv_prev",
                        "return_total", "pv_orig", "delta", "theta"]].
                   groupby(["symbol"]).
                   agg({
                       "return_today": "sum",
                       "return_total": "sum",
                       "market_value": "sum",
                       "pv_prev": "sum",
                       "pv_orig": "sum",
                       "delta": "sum",
                       "theta": "sum"}).
                   sort_values(["symbol"]) )


    #
    # compbine all data together
    #
    a1 = agg_oos.index.values
    a2 = agg_oes.index.values
    a3 = agg_ops.index.values

    symbols = np.unique(np.concatenate([a1, a2, a3], axis=None))

    df = pd.DataFrame()
    df["symbol"] = symbols

    df = df.join(agg_oos[["oo_total"]], on="symbol", how="left")
    df = df.join(agg_oes[["oe_total"]], on="symbol", how="left")
    df = df.join(agg_ops[["return_total", "return_today", "market_value",
                        "delta", "theta"]], on="symbol", how="left")
    df = df.fillna(0)

    df.rename(columns={'return_total': 'op_total'}, inplace=True)

    df["op_total"] = df["op_total"] * 100.0
    df["return_today"] = df["return_today"] * 100.0
    df["market_value"] = df["market_value"] * 100.0
    df["delta"] = df["delta"] * 100.0
    df["theta"] = df["theta"] * 100.0

    df["total"] = df.oo_total + df.oe_total + df.op_total

    df["positions"] = df["market_value"].abs().gt(0.0)

    cols = ["symbol", "oo_total", "oe_total", "op_total", "total",
            "return_today", "market_value", "delta", "theta", "positions"]

    return df[cols].sort_values(["positions", "total"])
