#
# World McCrea
# 5/22/2024
# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#
# Note: The miles and speed entered could be a floating point
# number.
#

# Get the number of miles.
miles = float(input('How many miles will you be travelling?: '))

# Get the speed in MPH.
speed = float(input('How many MPH will you be travelling?: '))

# Calculate the travel time.
travel_time = miles / speed

# Display the travel time (formatted to 2 decimal places).
print(f'You will reach your destination in{travel_time: .2f} hours.')
