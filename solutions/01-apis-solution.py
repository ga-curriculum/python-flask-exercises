# 7.1 Weather You Like It Or Not
# Complete the weather application below
import requests
command = ""
api_key = "YOUR_KEY_HERE"
while (command != "q"):
    command = input(
        "Choose [c] for current weather, [f] for a forecast, and [q] to quit.")
    if (command == "c"):
        location = input(
            "What location would you like the current weather for: ")
        # A. Use the location string to send a search query to this endpoint:
        # https://openweathermap.org/current#one
        # Then, print "The weather in _____ is _______ degrees" using the location and temperature result
        request_string = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        weather_result = requests.get(request_string)
        weather_result = weather_result.json()
        temperature = weather_result["main"]["temp"]
        temperature_in_fahrenheit = (temperature - 273.15) * 9/5 + 32
        print(f"The weather in {location} is {temperature_in_fahrenheit}")
    if (command == "f"):
        location = input("What location would you like a forecast for?")
        count = input("How many days would you like (choose up to 16)")
        # B. Use the location and count variables for a request to this endpoint:
        # https://openweathermap.org/forecast16#16days
        # Then, loop through the list and display each day's result however you'd like
        request_string = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt={count}&appid={api_key}"
        weather_result = requests.get(request_string)
        weather_result = weather_result.json()
        day_number = 1
        for result in weather_result["list"]:
            temperature = result["temp"]["day"]
            temperature_in_fahrenheit = (temperature - 273.15) * 9/5 + 32
            print(
                f"On day {day_number} it will be {temperature_in_fahrenheit} degrees during the day")
            day_number += 1
