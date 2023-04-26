import requests
from pprint import pprint

with open("api_key.txt", "r") as file:
    API_KEY = file.read()


def get_data(place):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    filter_by_day = {}
    for datapoint in filtered_data:
        date = datapoint["dt_txt"][:10]
        if date in filter_by_day.keys():
            filter_by_day[date].append(datapoint)
        else:
            filter_by_day[date] = []
            filter_by_day[date].append(datapoint)
    return filter_by_day


def get_12_hour(time_24):
    hours = int(time_24[:2])
    if hours > 12:
        return str(hours - 12) + time_24[2:] + " PM"
    if hours == 0:
        return "12" + time_24[2:] + " AM"
    if hours == 12:
        return time_24 + " PM"
    return time_24 + " AM"


if __name__ == "__main__":
    # pprint(get_data("Tokyo", None, None))
    data = get_data("Tokyo")
    pprint(data)
