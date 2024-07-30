#
# World McCrea
# 6/11/24
# This program shows my understanding of matplotlib


import matplotlib.pyplot as plt

# Ask the user for the title of the bar graph
title = input("Enter the bar graph title: ")

# Ask the user for labels for the x-axis and y-axis
x_label = input("Enter the label for the x-axis: ")
y_label = input("Enter the label for the y-axis: ")

# Ask user for number of data points
num_points = int(input("Enter the number of data points: "))

# empty lists for labels and values
labels = []
values = []

# Use a for loop to ask the user for data point labels and values
for i in range(num_points):
    label = input(f"Enter the name for tick {i+1}: ")
    value = float(input(f"Enter the value for tick {i+1}: "))
    labels.append(label)
    values.append(value)

# Create the bar graph
plt.bar(labels, values)

# Add a title for the chart
plt.title(title)

# Add labels for the x-axis and y-axis
plt.xlabel(x_label)
plt.ylabel(y_label)

# Display the bar graph
plt.show()

# The program terminates after the user closes the window displaying the bar graph
