from pathlib import Path

import math
import os
import time
import webbrowser

import folium
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

API_KEY = "YOUR_WEATHERAPI_KEY"

HISTORY_FILE = "travel_history.txt"
FAVORITES_FILE = "favorites.txt"

VEHICLES = {
    "Walking": 5,
    "Jogging": 10,
    "Bicycle": 20,
    "Motorcycle": 60,
    "Car": 80,
    "Barry Allen": 1000000
}

MET_VALUES = {
    "Walking": 3.0,
    "Jogging": 9.8,
    "Cycling": 7.0
}


def ensure_files():
    for file in [HISTORY_FILE, FAVORITES_FILE]:
        if not os.path.exists(file):
            open(file, "w").close()


def get_weather(city):
    try:
        response = requests.get(
            "http://api.weatherapi.com/v1/current.json",
            params={"key": API_KEY, "q": city},
            timeout=10
        )

        data = response.json()

        if "error" in data:
            print("Location not found.")
            return

        print("\n--- WEATHER REPORT ---")
        print("City:", data["location"]["name"])
        print("Country:", data["location"]["country"])
        print("Temperature:", data["current"]["temp_c"], "°C")
        print("Humidity:", data["current"]["humidity"], "%")
        print("Condition:", data["current"]["condition"]["text"])
        print("-" * 30)

    except Exception as e:
        print("Weather lookup failed:", e)


def get_locations(location1, location2):
    try:
        geolocator = Nominatim(user_agent="can_i_walk_there")
        place1 = geolocator.geocode(location1)
        place2 = geolocator.geocode(location2)

        if not place1 or not place2:
            return None, None

        return place1, place2

    except Exception as e:
        print("Location lookup failed:", e)
        return None, None


def hard_distance(place1, place2):
    lat1 = math.radians(place1.latitude)
    lon1 = math.radians(place1.longitude)

    lat2 = math.radians(place2.latitude)
    lon2 = math.radians(place2.longitude)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return 6371 * c


def easy_distance(place1, place2):
    coords1 = (place1.latitude, place1.longitude)
    coords2 = (place2.latitude, place2.longitude)
    return geodesic(coords1, coords2).km


def save_history(location1, location2):
    t = time.localtime()

    entry = (
        f"{location1} -> {location2} | "
        f"{t.tm_mday:02d}/{t.tm_mon:02d}/{t.tm_year} "
        f"{t.tm_hour:02d}:{t.tm_min:02d}"
    )

    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")


def show_history():
    with open(HISTORY_FILE, "r") as file:
        print("\n--- HISTORY ---")
        print(file.read())


def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared.")


def add_favorite():
    location = input("Location: ")
    with open(FAVORITES_FILE, "a") as file:
        file.write(location + "\n")


def show_favorites():
    with open(FAVORITES_FILE, "r") as file:
        print("\n--- FAVORITES ---")
        print(file.read())


def clear_favorites():
    open(FAVORITES_FILE, "w").close()
    print("Favorites cleared.")


def travel_time(distance):
    print("\n--- TRAVEL TIMES ---")

    for vehicle, speed in VEHICLES.items():
        hours = distance / speed
        print(f"{vehicle:<12}: {hours:.2f} hours")


def calories_burned(hours):
    weight = float(input("Weight (kg): "))

    print("\n--- CALORIES ---")

    for activity, met in MET_VALUES.items():
        calories = met * weight * hours
        print(f"{activity:<12}: {calories:.0f} calories")


def generate_map(place1, place2):
    coords1 = (place1.latitude, place1.longitude)
    coords2 = (place2.latitude, place2.longitude)

    m = folium.Map()

    folium.Marker(
        coords1,
        popup=place1.address,
        tooltip="Start"
    ).add_to(m)

    folium.Marker(
        coords2,
        popup=place2.address,
        tooltip="Destination"
    ).add_to(m)

    folium.PolyLine(
        [coords1, coords2],
        weight=4
    ).add_to(m)

    m.fit_bounds([coords1, coords2])

    filename = "route.html"
    m.save(filename)

    webbrowser.open(
        "file://" + os.path.realpath(filename)
    )

    print("Map generated.")


def display_results(place1, place2):
    haversine = hard_distance(place1, place2)
    geopy_distance = easy_distance(place1, place2)

    print("\n" + "=" * 50)

    print("\nLocation 1")
    print(place1.address)

    print("\nLocation 2")
    print(place2.address)

    print("\nHaversine Distance :", f"{haversine:.2f} km")
    print("Geopy Distance     :", f"{geopy_distance:.2f} km")
    print("Difference         :", f"{abs(haversine-geopy_distance):.2f} km")

    hours = haversine / 5

    print(f"\nEstimated Walking Time: {hours:.2f} hours")

    if haversine <= 2:
        print("Verdict: Easy walk")
    elif haversine <= 5:
        print("Verdict: Reasonable walk")
    elif haversine <= 15:
        print("Verdict: Long walk")
    elif haversine <= 30:
        print("Verdict: You're committed now")
    else:
        print("Verdict: Absolutely not")

    print("=" * 50)

    travel_time(haversine)

    if input("\nCalculate calories? (y/n): ").lower() == "y":
        calories_burned(hours)

    if input("\nGenerate map? (y/n): ").lower() == "y":
        generate_map(place1, place2)


def favorites_menu():
    while True:
        print("\n1. Add Favorite")
        print("2. View Favorites")
        print("3. Clear Favorites")
        print("4. Back")

        choice = input("Select: ")

        if choice == "1":
            add_favorite()
        elif choice == "2":
            show_favorites()
        elif choice == "3":
            clear_favorites()
        elif choice == "4":
            break


def history_menu():
    while True:
        print("\n1. View History")
        print("2. Clear History")
        print("3. Back")

        choice = input("Select: ")

        if choice == "1":
            show_history()
        elif choice == "2":
            clear_history()
        elif choice == "3":
            break


def main():
    ensure_files()

    while True:
        print("\n" + "=" * 35)
        print("CAN I WALK THERE? v1.0")
        print("=" * 35)

        print("1. Calculate Route")
        print("2. Weather Lookup")
        print("3. Favorites")
        print("4. Travel History")
        print("5. Quit")

        choice = input("\nSelect option: ")

        if choice == "1":
            location1 = input("Location 1: ")
            location2 = input("Location 2: ")

            place1, place2 = get_locations(location1, location2)

            if place1 is None:
                print("Location not found.")
                continue

            save_history(location1, location2)
            display_results(place1, place2)

        elif choice == "2":
            city = input("City: ")
            get_weather(city)

        elif choice == "3":
            favorites_menu()

        elif choice == "4":
            history_menu()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

path = "/mnt/data/can_i_walk_there_v1.py"
Path(path).write_text()

print(path)
