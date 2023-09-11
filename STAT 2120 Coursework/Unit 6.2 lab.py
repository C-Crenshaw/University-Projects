"""""""""""""""""""""""""""""""""""

Unit 6.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/coins_collection.csv"
coins = pd.read_csv(filename)

#%%
# Create population histogram
sns.distplot(coins.Age, bins=11, kde=False, color="blue", hist_kws=dict(edgecolor="black"))

plt.title("Histogram of age of coins")
plt.ylabel("Frequency")
plt.xlabel("Age")

#%%
# Draw your simple random sample
n = coins.sample(35)
print(n)

n = random.choices(coins.Age, k=35)

#%%
# Calculate your sample mean
xbar = np.mean(n)
print(xbar)

#%%
# Determine z*
z_star = stats.norm.ppf(0.90)
z_star = round(z_star, 3)
print(z_star)

#%%
# Calculate your CI
sigma = 3.059924
n = 35

LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))

# Margin of Error

MOE = z_star * sigma/np.sqrt(n)
print(MOE)

#%% Question 9

xbar = (8.8104 + 11.1248)/2
print(xbar)

z_star = stats.norm.ppf(0.99)
print(z_star)

LL = xbar - z_star * (0.5904)
UL = xbar + z_star * (0.5904)

print(LL)
print(UL)


