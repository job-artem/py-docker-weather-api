import requests

API_KEY = "2aba40a7f9aa4bfaa97123256250602"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    print(f"Performing request to Weather API for city Paris...")

    params = {
        "key": API_KEY,
        "q": "Paris",
        "aqi": "no"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data.get("location", {}).get("name", "Unknown location")
        country = data.get("location", {}).get("country", "Unknown country")
        localtime = data.get("location", {}).get("localtime", "Unknown time")
        temp_c = data.get("current", {}).get("temp_c", "N/A")
        condition = data.get("current", {}).get("condition", {}).get("text", "Unknown condition")

        print(f"{location}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
