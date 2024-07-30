#
# World McCrea
# 5/22/2024
# This program calculates the time it takes to travel
# a certain distance going a specific speed.

# Bonus attempt using modulo and floor division
# to separate the hours from minutes in the output
#
# Note: The hours should output as integer, minutes should output wit 2 decimal points

# Get the number of miles.
miles = float(input('How many miles will you be travelling?: '))

# Get the speed in MPH.
speed = float(input('How many MPH will you be travelling?: '))

# Calculate the travel time.
travel_time = miles / speed

# Calculate travel time in minutes
minutes = travel_time * 60

# Separate the "hours" portion of the time using floor div
hours = int(minutes // 60)

# Separate the "minutes" portion of the time using modulo
leftover_min = int(minutes % 60)

# Display the travel time (formatted to 1 decimal place for hours
# 2 decimal places for minutes).

print(f'You will reach your destination in {hours} hours, and {leftover_min: .2f} minutes')
