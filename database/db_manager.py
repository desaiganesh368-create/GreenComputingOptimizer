import sqlite3


def create_database():
    connection = sqlite3.connect("data/system_data.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        cpu REAL,
        memory REAL,
        disk REAL,
        battery REAL,
        power REAL,
        carbon REAL,
        eco_score REAL
    )
""")

    connection.commit()
    connection.close()


def insert_system_data(
    system_data,
    power_usage,
    carbon_emission,
    eco_score
):
    connection = sqlite3.connect("data/system_data.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO system_usage (
            cpu,
            memory,
            disk,
            battery,
            power,
            carbon,
            eco_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        system_data["cpu"],
        system_data["memory"],
        system_data["disk"],
        system_data["battery"]
        if isinstance(system_data["battery"], (int, float))
        else None,
        power_usage,
        carbon_emission,
        eco_score
    ))

    connection.commit()
    connection.close()