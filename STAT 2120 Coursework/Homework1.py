#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:32:48 2022

@author: CarsonCrenshaw
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

#%% Question 1
# Read in the data values and sort them.
filename = "/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/DelayedFlights_IAD.csv"
flights = pd.read_csv(filename, index_col=0)
print(flights)

# Finding the max and min of the Arrival Delay column
np.min(flights['ArrDelay']) 

np.max(flights['ArrDelay'])

# Use the describe function to check
flights['ArrDelay'].describe()

# Finding the min of the Departure Delay column
np.min(flights['DepDelay']) 

# Five number summary of Arrival Delay column
flights['ArrDelay'].describe()

np.mean(flights['ArrDelay'])

np.std(flights['ArrDelay'])

# Confirm the correct data is presented
np.mean(flights['ArrDelay'])

np.median(flights['ArrDelay'])

# Creating a boxplot for Arrival Delay
box = sns.boxplot(y='ArrDelay', data=flights, width=0.5)
plt.setp(box.artists, fill=False, edgecolor="k")
plt.title("Arrival Delay Times from Washington Dulles International Airport (IAD) January - June 2008. ")

#%% Question 2

#Sort numbers in ascending order
numbers = [184, 224, 207, 193, 224, 213, 181, 193, 190, 219, 209, 185, 193, 209, 205, 223, 181, 194]
numbers.sort()
print(numbers)

np.median(numbers)

#%% Question 3

# Preg that do not last to term
mu = 266
sigma = 16

# Value of interest
x = 249

# Calculate the z-score
z = (x-mu)/sigma
print(z)

# Find the proportion to the left and round to four decimals.
prop = stats.norm.cdf(z)
prop = round(prop, 4)
print("The proportion of pregnancies that do not last to term (" + str(x) + ") is " + str(prop) + ".")

# Preg that last between 8 and 9 months
mu = 266
sigma = 16

x1 = 249
x2 = 280

# Calculate the z-scores
z1 = (x1-mu)/sigma
z2 = (x2-mu)/sigma
print(z1)
print(z2)

# Find the proportion between and round to four decimals.
prop = stats.norm.cdf(z2) - stats.norm.cdf(z1)
prop = round(prop, 4)
print("The proportion of pregnancies that end between term and full term (" + str(x1) + ") and (" + str(x2) + ") is " + str(prop) + ".")

# Shortest 20% of preg
mu = 266
sigma = 16

# Values of interest
prop_top = .20 

# Find the z-score with this proportion above it.
z = stats.norm.ppf(prop_top)

# Unstandardize z-score
x = z*sigma + mu
x = round(x, 1)
print("The shortest 20% are at least " + str(x) + " days long.")

# Longest 2% of preg
mu = 266
sigma = 16

# Values of interest
prop_top2 = .02
prop = 1 - prop_top2

# Find the z-score with this proportion above it.
z2 = stats.norm.ppf(prop)

# Unstandardize z-score
x2 = z2*sigma + mu
x2 = round(x2, 0)
print("The longest 2% are at least " + str(x2) + " days long.")
