#
# World McCrea
# 5/31/2024
# Pretty Pattern Generator
#
# NOTE: With the range functions, you may use 
# one, two, or three parameters to accomplish 
# your task.
FillThisIn = None  # Replace FillThisIn with correct code below

# Ask the user for the number of rows
num_rows = int(input('How many rows?'))
# Ask the user for the number of columns
num_columns = int(input('How many columns?'))

# Iterate over the rows.
# Use the input from the user. That's the only number it can be.
for row in range(num_rows): #this number depends on user input

    # Iterate over the columns.
    for col in range(num_columns): #user input
        # Test if the row and column are even numbered
        if row % 2 == 0 and col % 2 == 0:
            print(' ', end='')
        else:
            print('*', end='')

    # Go to the next row.
    print()
