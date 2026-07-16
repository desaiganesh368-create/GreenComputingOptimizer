import sqlite3
import matplotlib.pyplot as plt


def plot_cpu_graph():
    connection = sqlite3.connect("data/system_data.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, cpu
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    data.reverse()

    timestamps = [row[0] for row in data]
    cpu_values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, cpu_values, marker="o")

    plt.title("CPU Usage Trend")
    plt.xlabel("Time")
    plt.ylabel("CPU Usage (%)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_ram_graph():
    connection = sqlite3.connect("data/system_data.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, memory
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    data.reverse()

    timestamps = [row[0] for row in data]
    ram_values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))

    plt.plot(
        timestamps,
        ram_values,
        marker="o"
    )

    plt.title("RAM Usage Trend")
    plt.xlabel("Time")
    plt.ylabel("RAM Usage (%)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_power_graph():
    connection = sqlite3.connect("data/system_data.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, power
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    data.reverse()

    timestamps = [row[0] for row in data]
    power_values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))

    plt.plot(
        timestamps,
        power_values,
        marker="o"
    )

    plt.title("Power Consumption Trend")
    plt.xlabel("Time")
    plt.ylabel("Power Consumption (Watts)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_carbon_graph():
    connection = sqlite3.connect("data/system_data.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, carbon
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    data.reverse()

    timestamps = [row[0] for row in data]
    carbon_values = [row[1] for row in data]

    plt.figure(figsize=(10, 5))

    plt.plot(
        timestamps,
        carbon_values,
        marker="o"
    )

    plt.title("Carbon Emission Trend")
    plt.xlabel("Time")
    plt.ylabel("Carbon Emission (kg CO2/hour)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

def plot_eco_score_graph():
    connection = sqlite3.connect(
        "data/system_data.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, eco_score
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    connection.close()

    data.reverse()

    timestamps = [row[0] for row in data]
    eco_scores = [row[1] for row in data]

    plt.figure(figsize=(10, 5))

    plt.plot(
        timestamps,
        eco_scores,
        marker="o"
    )

    plt.title("Eco Score Trend")
    plt.xlabel("Time")
    plt.ylabel("Eco Score")

    plt.ylim(0, 100)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()