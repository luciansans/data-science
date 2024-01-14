# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:40:48 2023

@author: Lucian
"""

import numpy as np
from scipy.stats import skew

# Results_PRO511 array
Results_PRO511 = np.array([55, 78, 90, 50, 45, 67, 88, 43, 68, 91, 68, 70, 81, 64, 73, 83, 40, 18, 61, 94])

# a. Sort and determine the size of the list; display the results
sorted = np.sort(Results_PRO511)
size_of_list = len(Results_PRO511)
print(f"a. Sorted Results: {sorted}")
print(f"   Size of the List: {size_of_list}")

# b. Calculate and display the mean and median
mean_result = np.mean(Results_PRO511)
median_result = np.median(Results_PRO511)
print(f"b. Mean: {mean_result:.2f}")
print(f"   Median: {median_result}")

# c. Calculate and display the min and max
min = np.min(Results_PRO511)
max = np.max(Results_PRO511)
print(f"c. Min: {min}")
print(f"   Max: {max}")

# d. Calculate and display the standard deviation and variance
std_deviation = np.std(Results_PRO511)
variance = np.var(Results_PRO511)
print(f"d. Standard Deviation: {std_deviation:.2f}")
print(f"   Variance: {variance:.2f}")

# e. Calculate the skew of the data and display the type of skewness was on scope not in learning guide 
skewness = skew(Results_PRO511)
skewness_type = "Positive Skew" if skewness > 0 else "Negative Skew" if skewness < 0 else "No Skew"
print(f"e. Skewness: {skewness:.2f}")
print(f"   Skewness Type: {skewness_type}")
