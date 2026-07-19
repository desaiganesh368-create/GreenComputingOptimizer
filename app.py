import pandas as pd

import sqlite3

from flask import jsonify, send_file
from flask import Flask, render_template

from utils.system_collector import collect_system_data
from energy.power_calculator import calculate_power_consumption
from energy.carbon_calculator import calculate_carbon_emission
from energy.eco_score import (
    calculate_eco_score,
    get_eco_status
)
from recommendations.recommendation_engine import generate_recommendations

from monitor.process_monitor import get_top_processes
from energy.process_energy import classify_process_energy

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from ml.prediction import (
    predict_cpu_usage,
    predict_power_usage
)



app = Flask(__name__)


@app.route("/")
def home():
    system_data = collect_system_data()

    power_usage = calculate_power_consumption(
        system_data["cpu"],
        system_data["memory"]
    )

    carbon_emission = calculate_carbon_emission(
        power_usage
    )

    eco_score = calculate_eco_score(
        system_data["cpu"],
        system_data["memory"],
        power_usage,
        carbon_emission
    )

    eco_status = get_eco_status(
        eco_score
    )

    recommendations = generate_recommendations(
        system_data
    )

    predicted_cpu_usage = predict_cpu_usage()
    predicted_power = predict_power_usage()

    processes = get_top_processes()

    for process in processes:
        process["energy"] = classify_process_energy(
            process["cpu"]
        )

    return render_template(
        "index.html",
        cpu=system_data["cpu"],
        memory=system_data["memory"],
        disk=system_data.get("disk", 0),
        battery=system_data["battery"],
        power=power_usage,
        carbon=carbon_emission,
        eco_score=eco_score,
        eco_status=eco_status,
        recommendations=recommendations,
        processes=processes,
        predicted_cpu=predicted_cpu_usage,
        predicted_power=predicted_power
    )



@app.route("/chart-data")
def chart_data():
    connection = sqlite3.connect("data/system_data.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            timestamp,
            cpu,
            memory,
            power,
            carbon,
            eco_score
        FROM system_usage
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    connection.close()

    rows.reverse()

    data = {
        "timestamps": [row[0] for row in rows],
        "cpu": [row[1] for row in rows],
        "memory": [row[2] for row in rows],
        "power": [row[3] for row in rows],
        "carbon": [row[4] for row in rows],
        "eco_score": [row[5] for row in rows]
    }

    return jsonify(data)

@app.route("/live-data")
def live_data():
    system_data = collect_system_data()

    power_usage = calculate_power_consumption(
        system_data["cpu"],
        system_data["memory"]
    )

    carbon_emission = calculate_carbon_emission(
        power_usage
    )

    eco_score = calculate_eco_score(
        system_data["cpu"],
        system_data["memory"],
        power_usage,
        carbon_emission
    )

    eco_status = get_eco_status(
        eco_score
    )

    return {
        "cpu": system_data["cpu"],
        "memory": system_data["memory"],
        "disk": system_data.get("disk", 0),
        "battery": system_data["battery"],
        "power": power_usage,
        "carbon": carbon_emission,
        "eco_score": eco_score,
        "eco_status": eco_status
    }

@app.route("/download-csv")
def download_csv():

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    query = """
        SELECT *
        FROM system_usage
    """

    dataframe = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    file_path = "exports/system_report.csv"

    dataframe.to_csv(
        file_path,
        index=False
    )

    return send_file(
        file_path,
        as_attachment=True
    )

@app.route("/download-pdf")
def download_pdf():

    pdf_path = "reports/system_report.pdf"

    document = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Green Computing Optimizer Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    connection = sqlite3.connect(
        "data/system_data.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            AVG(cpu),
            AVG(memory),
            AVG(power),
            AVG(carbon),
            AVG(eco_score)
        FROM system_usage
    """)

    result = cursor.fetchone()

    connection.close()

    cpu_avg = round(result[0], 2)
    ram_avg = round(result[1], 2)
    power_avg = round(result[2], 2)
    carbon_avg = round(result[3], 4)
    eco_avg = round(result[4], 2)

    report_data = [
        f"Average CPU Usage: {cpu_avg}%",
        f"Average RAM Usage: {ram_avg}%",
        f"Average Power Usage: {power_avg} W",
        f"Average Carbon Emission: {carbon_avg} kg CO₂/hour",
        f"Average Eco Score: {eco_avg}/100"
    ]

    for item in report_data:
        story.append(
            Paragraph(
                item,
                styles["Normal"]
            )
        )

        story.append(
            Spacer(1, 10)
        )

    document.build(story)

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
