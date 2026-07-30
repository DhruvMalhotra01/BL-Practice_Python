cities = {
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "pune": (18.5204, 73.8567),
    "hyderabad": (17.3850, 78.4867)
}

# Function to search for a city
def check_city(city_name):
    city = city_name.lower()

    if city in cities:
        latitude, longitude = cities[city]
        return f"{city.title()}: Latitude = {latitude}, Longitude = {longitude}"
    else:
        return "City not found in the dictionary."


# Display dictionary
print("Cities Dictionary:")
print(cities)

# Run until user enters exit
while True:
    city_name = input("\nEnter a city name (or type 'exit' to quit): ")

    if city_name.lower() == "exit":
        print("Exiting the program.")
        break

    print(check_city(city_name))