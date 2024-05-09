import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import time

class SeoulBikeDataCollector:
    def __init__(self, service_key):
        self.service_key = service_key
        self.api_host = "http://openapi.seoul.go.kr:8088"
        self.api_type = "json"
        self.api_service = "bikeList"

    def request_seoul_api(self, start_index, end_index):
        url = f"{self.api_host}/{self.service_key}/{self.api_type}/{self.api_service}/{start_index}/{end_index}/"
        return requests.get(url)

    def collect_data(self):
        bike_stations = []
        for start_index in range(1, 2001, 1000):
            end_index = start_index + 999
            response = self.request_seoul_api(start_index, end_index)
            if response.status_code == 200:
                bike_stations.extend(response.json()["rentBikeStatus"]["row"])
        return bike_stations

    def save_to_csv(self, bike_stations):
        data_list = []
        for station in bike_stations:
            data = {
                "rackTotCnt": station["rackTotCnt"],
                "stationName": station["stationName"],
                "parkingBikeTotCnt": station["parkingBikeTotCnt"],
                "shared": station["shared"],
                "stationLatitude": station["stationLatitude"],
                "stationLongitude": station["stationLongitude"],
                "stationId": station["stationId"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            data_list.append(data)

        df = pd.DataFrame(data_list)
        df.to_csv('data/seoul_bike_stations.csv', index=False)
        print('Data saved to CSV.')

def main():
    load_dotenv('vidoe_sources/.env')
    service_key = os.getenv('DDAREUNGI_API_KEY')
    data_collector = SeoulBikeDataCollector(service_key)
    
    try:
        while True:  # Run the loop twice as an example
            bike_stations = data_collector.collect_data()
            data_collector.save_to_csv(bike_stations)
            time.sleep(60)  # Wait a minute before the next run
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
