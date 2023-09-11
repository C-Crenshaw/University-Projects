"""""""""""""""""""""""""""""""""""

Unit 6.3 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random as random

# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/coins_collection.csv"
coins = pd.read_csv(filename)


#%%
# Draw your simple random sample
sample_size = 35
samp_coins = coins.sample(n = sample_size)
print(samp_coins)

# another way to generate this sample
sample1 = random.choices(coins.Age, k=35)
print(sample1)

# and another way to draw a sample of 35
n = coins.sample(35)
print(n)

#%%
# Calculate sample mean
xbar = np.mean(samp_coins)
print(xbar)

#%%
# Calculate test statistic
sigma = 3.059924
n = 35
mu0 = 2.5

z = (xbar - mu0)/(sigma/np.sqrt(n))
print(z)

#%%
# Determine p-value, right-tailed
pval = 1-stats.norm.cdf(z)
print(pval)






