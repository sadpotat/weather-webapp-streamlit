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


if __name__ == "__main__":
    # pprint(get_data("Tokyo", None, None))
    data = get_data("Tokyo")
    pprint(data)
