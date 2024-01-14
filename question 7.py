# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:02:51 2023

@author: Lucian
"""

import pandas as pd
import matplotlib.pyplot as plt

# a. Read the file titled "breach_report.csv" and display the 'State', 'Breach Submission Date' and 'Type of Breach' columns.
file_path = "breach_report.csv"  
data = pd.read_csv(file_path, parse_dates=['Breach Submission Date'])

# Display the specified columns
selected_columns = ['State', 'Breach Submission Date', 'Type of Breach']
display_a = data[selected_columns]
print("a. Displaying 'State', 'Breach Submission Date', and 'Type of Breach' columns:")
print(display_a)

# b. Determine the total number of data breaches in the states mentioned above.
selected_states = ['NY', 'FL', 'TX']
filtered_data = data[data['State'].isin(selected_states)]
total_breaches = len(filtered_data)
print(f"\nb. Total number of data breaches in NY, FL, and TX: {total_breaches}")

# c. Plot a stacked bar graph based on the information obtained from b (Ensure the graph is labelled appropriately)
breach_counts = filtered_data['State'].value_counts()

# Plotting  bar graph
plt.bar(selected_states, breach_counts, color=['blue', 'green', 'red'])
plt.xlabel('States')
plt.ylabel('Number of Data Breaches')
plt.title('Number of Data Breaches in NY, FL, and TX (2009-2016)')
plt.show()
