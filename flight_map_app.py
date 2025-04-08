import streamlit as st
import pandas as pd
import json
import folium
from streamlit_folium import st_folium

df = pd.read_csv("data/black_sea_flights.csv")

with open("data/black_sea_flight_routes.json", "r", encoding="utf-8") as f:
    routes_data = json.load(f)

routes_dict = {entry["Callsign"]: entry["Route"] for entry in routes_data}

# Заголовок приложения
st.title("🛫 Интерактивная карта маршрутов самолётов")

# Фильтры
airline = st.selectbox("Выберите авиакомпанию", ["Все"] + sorted(df['Airline'].unique()))
callsign = st.selectbox("Выберите позывной", ["Все"] + sorted(df['Callsign'].unique()))

# Применение фильтров
filtered_df = df.copy()

if airline != "Все":
    filtered_df = filtered_df[filtered_df["Airline"] == airline]

if callsign != "Все":
    filtered_df = filtered_df[filtered_df["Callsign"] == callsign]

# Карта
m = folium.Map(location=[44.3, 47.3], zoom_start=3)

for _, row in filtered_df.iterrows():
    cs = row["Callsign"]
    icao = row["ICAO"]
    aircraft = row["Aircraft Model"]
    departure = row["Departure"]
    arrival =  row["Arrival"]
    route = routes_dict.get(cs, [])

    if route:
        points = [(p["lat"], p["lon"]) for p in route]

        folium.PolyLine(
            points,
            color="blue",
            weight=3,
            tooltip=f"{cs} | {aircraft} | {departure} –> {arrival}"
        ).add_to(m)

        folium.Marker(
            points[0],
            popup=f"{aircraft}",
            icon=folium.Icon(color="green", icon="plane", prefix="fa")
        ).add_to(m)

# Отображение карты в Streamlit
st_data = st_folium(m, width=1000, height=600)