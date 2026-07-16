import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_cpu_usage():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT cpu
        FROM system_usage
        ORDER BY id
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if len(dataframe) < 5:
       return 0

    x = np.arange(
        len(dataframe)
    ).reshape(-1, 1)

    y = dataframe["cpu"]

    model = LinearRegression()

    model.fit(
        x,
        y
    )

    next_value = model.predict(
        [[len(dataframe)]]
    )[0]

    next_value = max(
       0,
       min(next_value, 100)
    )

    return round(
        next_value,
        2
    )