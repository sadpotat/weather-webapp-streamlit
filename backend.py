import requests

with open("api_key.txt", "r") as file:
    API_KEY = file.read()


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    num_values = 8*forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == "__main__":
    # pprint(get_data("Tokyo", None, None))
    data = get_data("Tokyo", 3)
    print(data)
