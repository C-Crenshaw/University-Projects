"""""""""""""""""""""""""""""""""""

Unit 3 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd

# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/buildings.csv"
build = pd.read_csv(filename)

#%%
# Draw your simple random sample
# Define the sample size
my_n = 4

# Draw the random sample
samp_buildings = build.sample(n=my_n)
print(samp_buildings)

