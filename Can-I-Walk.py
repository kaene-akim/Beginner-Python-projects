import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_locations(location1, location2):

    geolocator = Nominatim(user_agent="can_i_walk_there")

    place1 = geolocator.geocode(location1)
    place2 = geolocator.geocode(location2)

    if not place1 or not place2:
        return None, None

    return place1, place2


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


def display_results(place1, place2):

    haversine_km = hard_distance(place1, place2)
    geopy_km = easy_distance(place1, place2)

    error = abs(haversine_km - geopy_km)

    print("\n" + "=" * 50)

    print("\nLocation 1")
    print(f"Name: {place1.address}")
    print(f"Latitude: {place1.latitude:.6f}")
    print(f"Longitude: {place1.longitude:.6f}")

    print("\nLocation 2")
    print(f"Name: {place2.address}")
    print(f"Latitude: {place2.latitude:.6f}")
    print(f"Longitude: {place2.longitude:.6f}")

    print("\n" + "=" * 50)

    print(f"\nYour Haversine Distance : {haversine_km:.2f} km")
    print(f"Geopy Distance          : {geopy_km:.2f} km")
    print(f"Difference              : {error:.2f} km")

    hours = haversine_km / 5

    print(f"\nEstimated Walking Time: {hours:.1f} hours")

    if haversine_km <= 2:
        print("Verdict: Easy walk.")
    elif haversine_km <= 5:
        print("Verdict: Reasonable walk.")
    elif haversine_km <= 15:
        print("Verdict: Long walk. Bring water.")
    elif haversine_km <= 30:
        print("Verdict: You're committed now.")
    else:
        print("Verdict: Absolutely not.")

    print("\n" + "=" * 50)


def menu():

    while True:

        choice = input(
            "\n"
            + "=" * 35 +
            "\n      CAN I WALK THERE?"
            "\n" + "=" * 35 +
            "\n1. Find distance(one is calculated by me, the other is a boring corporate answer)"
            "\n2. Quit"
            "\n\nSelect option: "
        )

        if choice == "1":

            location1 = input("\nEnter location 1: ")
            location2 = input("Enter location 2: ")

            place1, place2 = get_locations(location1, location2)

            if place1 is None:
                print("\nOne or both locations could not be found.")
                continue

            display_results(place1, place2)

        elif choice == "2":

            print("\nGoodbye.")
            break

        else:

            print("\nInvalid option.")


menu()