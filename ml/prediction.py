import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.ensemble import RandomForestRegressor


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

def predict_power_usage():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT power
        FROM system_usage
        ORDER BY id
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if len(dataframe) < 5:
        return None

    x = np.arange(
        len(dataframe)
    ).reshape(-1, 1)

    y = dataframe["power"]

    model = LinearRegression()

    model.fit(
        x,
        y
    )

    prediction = model.predict(
        [[len(dataframe)]]
    )[0]

    return round(
        prediction,
        2
    )

def predict_carbon_emission():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT carbon
        FROM system_usage
        ORDER BY id
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if len(dataframe) < 5:
        return None

    x = np.arange(
        len(dataframe)
    ).reshape(-1, 1)

    y = dataframe["carbon"]

    model = LinearRegression()

    model.fit(
        x,
        y
    )

    prediction = model.predict(
        [[len(dataframe)]]
    )[0]

    return round(
        prediction,
        4
    )

def predict_eco_score():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT eco_score
        FROM system_usage
        ORDER BY id
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if len(dataframe) < 5:
        return None

    x = np.arange(
        len(dataframe)
    ).reshape(-1, 1)

    y = dataframe["eco_score"]

    model = LinearRegression()

    model.fit(
        x,
        y
    )

    prediction = model.predict(
        [[len(dataframe)]]
    )[0]

    prediction = max(
        0,
        min(100, prediction)
    )

    return round(
        prediction,
        2
    )


def prepare_training_data(dataframe):
    dataframe = dataframe.copy()

    dataframe["target_cpu"] = (
        dataframe["cpu"].shift(-1)
    )

    dataframe = dataframe.dropna()

    features = dataframe[
        [
            "cpu",
            "memory",
            "disk",
            "power",
            "carbon",
            "eco_score"
        ]
    ]

    target = dataframe["target_cpu"]

    return features, target

def predict_cpu_random_forest():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT
            cpu,
            memory,
            disk,
            power,
            carbon,
            eco_score
        FROM system_usage
        ORDER BY id
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if len(dataframe) < 20:
        return None

    X, y = prepare_training_data(
        dataframe
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X,
        y
    )

    latest_sample = X.iloc[[-1]]

    prediction = model.predict(
        latest_sample
    )[0]

    return round(
        prediction,
        2
    )

