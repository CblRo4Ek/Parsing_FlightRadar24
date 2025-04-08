import pandas as pd
import json
from datetime import datetime


def build_data_showcases():
    flights_df = pd.read_csv("data/black_sea_flights.csv")

    with open("data/black_sea_flight_routes.json", "r", encoding="utf-8") as f:
        route_data = json.load(f)

    callsign_to_time = {}

    for flight in route_data:
        callsign = flight["Callsign"]
        route = flight["Route"]

        if route:
            timestamps = [pt["ts"] for pt in route if pt.get("ts")]
            if timestamps:
                first_time = min(timestamps)
                callsign_to_time[callsign] = datetime.utcfromtimestamp(first_time)

    # Добавляем столбцы даты и часа
    flights_df["Datetime"] = flights_df["Callsign"].map(callsign_to_time)
    flights_df["Date"] = flights_df["Datetime"].dt.date
    flights_df["Hour"] = flights_df["Datetime"].dt.hour

    # Удалим пустые значения времени
    flights_df = flights_df.dropna(subset=["Datetime"])

    # 1. Кол-во рейсов по авиакомпаниям за день
    by_airline_day = flights_df.groupby(["Date", "Airline"]).size().reset_index(name="Flight Count")
    by_airline_day.to_csv("data/flights_by_airline_per_day.csv", index=False)

    # 2. Кол-во рейсов по моделям самолётов за день
    by_model_day = flights_df.groupby(["Date", "Aircraft Model"]).size().reset_index(name="Flight Count")
    by_model_day.to_csv("data/flights_by_model_per_day.csv", index=False)

    # За каждый час — (Airline + Aircraft)
    by_hour_airline = flights_df.groupby(["Date", "Hour", "Airline"]).size().reset_index(name="Flight Count")
    by_hour_model = flights_df.groupby(["Date", "Hour", "Aircraft Model"]).size().reset_index(name="Flight Count")

    by_hour_airline.to_csv("data/flights_by_airline_per_hour.csv", index=False)
    by_hour_model.to_csv("data/lights_by_model_per_hour.csv", index=False)

    print("Витрины созданы")
