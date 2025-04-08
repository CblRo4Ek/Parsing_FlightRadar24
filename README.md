# ✈️ Мониторинг акватории Чёрного моря

Проект для получения и анализа данных о воздушных рейсах, проходящих над акваторией Чёрного моря. Используется API FlightRadar24 для сбора информации о рейсах, построения маршрутных данных и создания витрин по авиакомпаниям и моделям самолётов.

---

## 📦 Структура проекта

Техническое задание находится в файле **ТЗ.pdf**
* **main.py** – основной скрипт, сочетающий в себе загрузку данных с FlightRadar24 с последующим сохранением их в файлы (**data_import.py**) и создание витрин (**data_showcase.py**)
* **data_import.py** – загрузка данных с FlightRadar24 с последующим сохранением их в csv файлы
* **data_showcase.py** – создание витрин данных, подсчитывающих количество рейсов по моделям самолётов и авиакомпаниям в заданной акватории за час/день
* **flight_map_app.py** – интерактивная карта на Folium + Streamlit
---

## 🚀 Быстрый старт

### 1. Клонируйте или скачайте проект

```bash
git clone https://...
```

```bash
cd Parsing_FlightRadar24
```

### 2. Создайте виртуальное окружение

```bash
python -m venv venv
```

### 3. Активируйте виртуальное окружение

* **Windows:**
```bash
venv\Scripts\activate
```

* **Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Установите зависимости

```bash
pip install -r requirements.txt
```

### 5. Запустите основной скрипт

```bash
python main.py
```

#### 🧾 Результаты

После выполнения **main.py** появится папка **data**, в которой появятся следующие файлы:

* **black_sea_flights.csv** – информация о рейсах над чёрным морем
* **black_sea_flight_routes.json** – географические точки маршрута
* **flights_by_airline_per_day.csv** – количество рейсов по авиакомпаниям за день
* **flights_by_model_per_day.csv** – количество рейсов по моделям самолётов за день
* **flights_by_airline_per_hour.csv** – количество рейсов по авиакомпаниям по часам
* **flights_by_model_per_hour.csv** – количество рейсов по моделям самолётов по часам

### 6. Запустите скрипт с интерактивной картой

```bash
streamlit run flight_map_app.py
```
