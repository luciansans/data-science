# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:21:57 2023

@author: Xray
"""
#a. Draw a scatter plot with the line of best fit. (Ensure the plot is labelled correctly.)
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 4, 5]

# Plot the scatter plot
plt.scatter(x_values, y_values, label='Data Points')

# Fit a linear regression line
slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
line = slope * np.array(x_values) + intercept

# Plot the line of best fit
plt.plot(x_values, line, color='red', label='Line of Best Fit')


# Label the plot
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot with Line of Best Fit')
plt.legend()

# Show the plot
plt.show()



#b. Determine the slope and intercept of the data
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")

#c. Predict and display the next five values
next_five_values = [slope * x + intercept for x in range(6, 11)]
print("Predicted Next Five Values:", next_five_values)

#d. d. Update the plot drawn to include the predicted values
# Update the scatter plot
plt.scatter(x_values, y_values, label='Data Points')

# Update the line of best fit
plt.plot(x_values, line, color='red', label='Line of Best Fit')

# Plot the predicted values
plt.scatter(range(6, 11), next_five_values, color='green', label='Predicted Values')


