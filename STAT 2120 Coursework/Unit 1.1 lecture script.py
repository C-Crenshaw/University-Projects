"""""""""""""""""""""""""""""""""""""""

Unit 1.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd


#%%
"""""""""""""""""""""""""""""""""""""""
Find the median
"""""""""""""""""""""""""""""""""""""""
# Read in the data values and sort them.
filename = "/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/federer_data.xlsx"
fed = pd.read_excel(filename, index_col=0)
fed_sort = fed.sort_values(by=['Percentage'])
print(fed_sort)

#%%
# Are there an even or odd number of data points?
n = fed.shape[0]
print(n)

#%%
# What is the location of the median?
med_loc = (n+1)/2
print(med_loc)

# If there are an odd number of data points, the median is one of the data points.
# If there are an even number of data points, the median is the average of two of the data points.

#%%
# Find and print the median.
i = [8,9]
med = np.mean(fed_sort.iloc[i])
print("Median is " + str(med.values[0]))

#%%
# Check the median by finding the correct location in the sorted data frame.
print("Check: median is " + str(med_loc) + "th ordered observation.")
print(fed_sort)

#%%
# Calculate and print the median using Python.
print(np.median(fed.Percentage))

#%%
"""""""""""""""""""""""""""""""""""""""
Find the mean
"""""""""""""""""""""""""""""""""""""""
# Calculate and print the mean using Python.
print(np.mean(fed.Percentage))


#%%
"""""""""""""""""""""""""""""""""""""""
Find the quartiles and IQR
"""""""""""""""""""""""""""""""""""""""
# Remember the location of the median.
print(med_loc)

#%%
# Separate the data into lists based on the median value.
fed_sort_Q1 = fed_sort[0:9]
fed_sort_Q3 = fed_sort[9:]
print(fed_sort_Q1)
print(fed_sort_Q3)

#%%
# Quartiles are the medians of the subset lists.
q_n = fed_sort_Q1.shape[0]
q_loc = (q_n + 1)/2
print(q_loc)

#%% 
# Find and print quartiles.
j = 4
Q1 = fed_sort_Q1.iloc[j]
Q3 = fed_sort_Q3.iloc[j]
print("Q1 is " + str(Q1.values[0]))
print("Q3 is " + str(Q3.values[0]))

#%%
# Find the IQR
IQR = Q3 - Q1
print("IQR is " + str(IQR.values[0]))

#%%
# Calculate the quartiles using Python.
Q1_py = np.percentile(fed.Percentage, 25)
Q3_py = np.percentile(fed.Percentage, 75)
print(Q1_py)
print(Q3_py)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 1.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

flight = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/flight.csv")
fed = pd.read_excel(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/federer_data.xlsx", index_col=0)
height = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/heights.csv")

#%%
"""""""""""""""""""""""""""""""""""""""
Create bar graph
"""""""""""""""""""""""""""""""""""""""
# With counts
sns.countplot(x="Destination", data=flight)
plt.title("Flight destinations")

#%% 
# With proportions
sns.barplot(x="Destination", data=flight, y="Delay (min)", orient="v", estimator=lambda x: len(x)/len(flight))
plt.ylabel("Proportion")

#%%
"""""""""""""""""""""""""""""""""""""""
Create boxplot
"""""""""""""""""""""""""""""""""""""""
box = sns.boxplot(y='Percentage', data=fed, width=0.5)
plt.setp(box.artists, fill=False, edgecolor="k")
plt.title("Roger Federer first-serve percentage 2001-2018")

#%%
"""""""""""""""""""""""""""""""""""""""
Create histogram
"""""""""""""""""""""""""""""""""""""""
# Lecure slides show histograms with 7, 4, and 5 bins, respectively.
sns.distplot(flight['FlightLength (min)'], bins=7, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of flight lengths")
plt.ylabel("Frequency")

#%%
sns.distplot(height['x'], bins=7, kde=False, color="white", hist_kws=dict(edgecolor="gray"))
plt.title("Histogram of 16-year-old girl heights")
plt.xlabel("Height (inches)")
plt.ylabel("Frequency")

#%%
"""""""""""""""""""""""""""""""""""""""
Create histogram with density
"""""""""""""""""""""""""""""""""""""""
den = sns.distplot(height['x'], bins=7, norm_hist=True, kde=False, color="white", hist_kws=dict(edgecolor="gray"))
plt.title("Histogram of 16-year-old girl heights")
plt.xlabel("Height (inches)")
plt.ylabel("Density")

#Add heights
den.text(58.5, 0.041, "0.04")
den.text(60.3, 0.056, "0.055")
den.text(62.5, 0.091, "0.09")
den.text(64.3, 0.116, "0.115")
den.text(66.5, 0.101, "0.10")
den.text(68.3, 0.076, "0.075")
den.text(70.3, 0.026, "0.025")
