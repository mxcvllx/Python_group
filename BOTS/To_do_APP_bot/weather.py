from datetime import datetime
import json

from environs import Env

import requests

env = Env()
env.read_env()


class WeatherManager:
    API_KEY = env("API_KEY")

    def __init__(self, city=None):
        self.city = city

    @staticmethod
    def convert_to_datetime(date_str):
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

    def get_data(self):
        url = f"https://api.tomorrow.io/v4/weather/forecast?" \
              f"location={self.city}&apikey={self.API_KEY}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)

    def get_timelines(self):
        res = self.get_data()
        return res.get("timelines")

    def get_daily_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("daily")

    def get_hourly_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("hourly")

    def get_day_hours_temperature_with_time(self, day_date):
        hourly_data = self.get_hourly_data()
        data = []

        for hour_data in hourly_data:
            time = hour_data.get("time")
            if self.convert_to_datetime(time).date() == day_date.date():
                data.append({
                    "time": self.convert_to_datetime(time).strftime("%H:%M"),
                    "temperature": hour_data["values"].get("temperature")
                })
        return data

    def get_daily_temperature(self):
        # data = []
        # for day in self.get_daily_data():
        #     day_values = day.get("values")
        #     average_temperature = None
        #     if day_values:
        #         average_temperature = day_values.get("temperatureAvg")
        #     day_date = datetime.strptime(day.get("time"), "%Y-%m-%dT%H:%M:%SZ")
        #     data.append({
        #         "day": day_date.strftime("%Y.%m.%d"),
        #         "average_temperature": average_temperature,
        #         "hours": self.get_day_hours_temperature_with_time(day_date)
        #     })
        #
        # return data

        # From JSON file
        with open("../api/weather.json") as f:
            return json.load(f)


city_weather = WeatherManager("tashkent")