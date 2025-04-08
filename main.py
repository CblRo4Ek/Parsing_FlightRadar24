import data_import
import data_showcase


if __name__ == "__main__":
    print("Загружаем данные с FlightRadar24...")
    data_import.fetch_flight_data()

    print("\nФормируем витрины данных...")
    data_showcase.build_data_showcases()
