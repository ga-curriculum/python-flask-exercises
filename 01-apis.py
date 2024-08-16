# 1.1 Weather You Like It Or Not
# Complete the weather application below

command = ""
while (command != "q"):
    command = input(
        "Choose [c] for current weather, [f] for a forecast, and [q] to quit.")
    if (command == "c"):
        location = input(
            "What location would you like the current weather for: ")
        # A. Use the location string to send a search query to this endpoint:
        # https://openweathermap.org/current#one
        # Then, print "The weather in _____ is _______ degrees" using the location and temperature result
    if (command == "f"):
        location = input("What location would you like a forecast for?")
        count = input("How many days would you like (choose up to 16)")
        # B. Use the location and count variables for a request to this endpoint:
        # https://openweathermap.org/forecast16#16days
        # Then, loop through the list and display each day's result however you'd like


# 1.2 API Scavenger Hunt
# Use any API from the link below and make requests to answer as many questions as you can
# https://github.com/public-apis/public-apis


# A. How many Yen will my $100 US Dollars convert to at today's exchange rates?


# B. How many shares of MSFT can I buy for that same $100?


# C. When is the next train arriving at _______? (choose any location)


# D. Find me a job posting to help my unemployed Graphic Designer friend.


# E. My roommate says they study "epistemology". What does that even mean?
