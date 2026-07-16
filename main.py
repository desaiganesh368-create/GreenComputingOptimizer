import time

from utils.system_collector import collect_system_data
from database.db_manager import (
    create_database,
    insert_system_data
)
from energy.power_calculator import calculate_power_consumption
from energy.carbon_calculator import calculate_carbon_emission
from energy.eco_score import (
    calculate_eco_score,
    get_eco_status
)
from recommendations.recommendation_engine import generate_recommendations
from energy.process_energy import classify_process_energy
from dashboard.charts import (
    plot_cpu_graph,
    plot_eco_score_graph,
    plot_ram_graph,
    plot_power_graph,
    plot_carbon_graph
)


create_database()

for _ in range(5):

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

    insert_system_data(
    system_data,
    power_usage,
    carbon_emission,
    eco_score
)

    recommendations = generate_recommendations(
    system_data
)

    print("\n===== GREEN COMPUTING OPTIMIZER =====\n")

    print(f"CPU Usage: {system_data['cpu']}%")
    print(f"RAM Usage: {system_data['memory']}%")
    print(f"Disk Usage: {system_data['disk']}%")
    print(f"Estimated Power Consumption: {power_usage} Watts")
    print(f"Estimated Carbon Emission: {carbon_emission} kg CO2/hour")
    print(
    f"Eco Score: {eco_score}/100 ({eco_status})"
)
    print("\nRecommendations:")

    for recommendation in recommendations:
        print(f"- {recommendation}")

    if isinstance(system_data["battery"], str):
       print(f"Battery Status: {system_data['battery']}")
    else:
       print(f"Battery Usage: {system_data['battery']}%")

    print("\nTop Processes:")

    for process in system_data["processes"]:

      energy_level = classify_process_energy(
        process["cpu"]
    )

    print(
        f"{process['name']} | "
        f"CPU: {process['cpu']}% | "
        f"RAM: {process['memory']:.2f}% | "
        f"Energy: {energy_level}"
    )

    print("\n" + "=" * 50 + "\n")

    time.sleep(10)

    plot_cpu_graph()

    plot_ram_graph()

    plot_power_graph()

    plot_carbon_graph()

    plot_eco_score_graph()