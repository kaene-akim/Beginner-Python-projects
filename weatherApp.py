import requests

API_KEY = "8bed5e1379f644a4bdc73418261706"

def get_weather(city):
    url = "http://api.weatherapi.com/v1/current.json"

    response = requests.get(url, params={
        "key": API_KEY,
        "q": city
    })

    # 1. HTTP-level check
    if response.status_code != 200:
        print(f"Request failed (HTTP {response.status_code})")
        return

    data = response.json()

    # 2. API-level error check
    if "error" in data:
        print("Location not found. Try again.")
        return

    # 3. Extract safely
    location = data["location"]
    current = data["current"]

    print("\n--- Weather Report ---")
    print("City:", location["name"])
    print("Country:", location["country"])
    print("Temperature:", current["temp_c"], "°C")
    print("Condition:", current["condition"]["text"])
    print("Humidity:", current["humidity"], "%")
    print("----------------------\n")


while True:
    city = input("Enter a city (or 'quit' to exit): ")

    if city.lower() == "quit":
        break

    get_weather(city)

        



