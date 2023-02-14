import requests
from BOTS.Weather_APP_bot.config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        print(data)
    except Exception as ex:
        print(ex)
        print("Проверте название города")


def main():
    city = input("Введите город")
    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
