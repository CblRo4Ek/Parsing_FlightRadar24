from FlightRadar24 import FlightRadar24API
import pandas as pd
import time
import json
import os


def fetch_flight_data():
    api = FlightRadar24API()
    bounds = "47.5,41.0,27.0,42.5"

    flights = api.get_flights(bounds=bounds)

    data = []
    trail_data = []

    for flight in flights:
        try:
            # Получаем подробную информацию о рейсе
            flight_details = api.get_flight_details(flight)

            # Работает как словарь
            identification = flight_details.get("identification", {})
            aircraft_info = flight_details.get("aircraft", {})
            airline_info = flight_details.get("airline", {})
            airport_info = flight_details.get("airport", {})
            trail = flight_details.get("trail", [])

            callsign = identification.get("callsign", "")
            icao = aircraft_info.get("hex", "")
            aircraft_model = aircraft_info.get("model", {}).get("text", "")
            airline = airline_info.get("name", "")

            origin = airport_info.get("origin", {}).get("code", {}).get("iata") or \
                     airport_info.get("origin", {}).get("code", {}).get("icao")
            destination = airport_info.get("destination", {}).get("code", {}).get("iata") or \
                          airport_info.get("destination", {}).get("code", {}).get("icao")

            # Траектория
            route_points = [
                {
                    "lat": point.get("lat"),
                    "lon": point.get("lng"),
                    "alt": point.get("alt"),
                    "ts": point.get("ts")
                }
                for point in trail
                if point.get("lat") is not None and point.get("lng") is not None
            ]

            if callsign:
                data.append({
                    "Callsign": callsign,
                    "ICAO": icao,
                    "Aircraft Model": aircraft_model,
                    "Airline": airline,
                    "Departure": origin,
                    "Arrival": destination,
                    "Count_route_points": len(route_points)
                })

                trail_data.append({
                    "Callsign": callsign,
                    "Route": route_points
                })

                print(f"Обработан рейс {callsign}")
                time.sleep(0.5)

        except:
            continue

    # Сохраняем данные
    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv("data/black_sea_flights.csv", index=False, encoding="utf-8-sig")

    with open("data/black_sea_flight_routes.json", "w", encoding="utf-8") as f:
        json.dump(trail_data, f, ensure_ascii=False, indent=2)

    print("Данные сохранены")
