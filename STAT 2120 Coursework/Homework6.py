#%% Question 1.1

# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats
import random as random

# Population parameters
mu = 355.5
sigma = 0.6

xbar = 355
z = (xbar - mu)/(sigma)

P1 = stats.norm.cdf(z)
P1 = round(P1, 4)
print(1-P1)

#%% 1.2
# Population parameters
mu = 355.5
sigma = 0.6
n = 6

xbar = 355
z = (xbar - mu)/(sigma/np.sqrt(n))
print(z)

P1 = stats.norm.cdf(z)
P1 = round(P1, 4)
print(1-P1)

#%% 1.3
mu = 355.5
sigma = 0.6
n = 6

xbar = 355.25
z = (xbar - mu)/(sigma/np.sqrt(n))
print(z)

P2 = stats.norm.cdf(z)
P2 = round(P2, 4)
print(P2)

#%% Question 2.1

chol = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/cholesterol.csv")

# Given information
sigma = 47.7
n = 37
xbar = np.mean(chol.level) 
print(xbar)

# Determine z*
z_star = stats.norm.ppf(0.995)
z_star = round(z_star, 3)
print(z_star)

# Determine confidence interval (lower limit and upper limit)
LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(LL)
print(UL)

MOE = z_star * sigma/np.sqrt(n)
print(MOE)

#%% 2.6
m_star = 20
sigma = 47.7
xbar = np.mean(chol.level) 
print(xbar)

# Determine z*
z_star = stats.norm.ppf(0.995)
z_star = round(z_star, 3)
print(z_star)

n = (z_star * sigma / m_star)**2
n = np.ceil(n)
print(n)

#%% Question 3.2

# known values, Normally distributed
sigma = 47.7
n = 37

# Null hypothesis
mu0 = 225

# Test statistic
xbar = np.mean(chol.level)
test_stat = (xbar - mu0)/(sigma/np.sqrt(n))
print(test_stat)

# p-value; test is one-sided, right tailed
pval = stats.norm.cdf(test_stat)
print(1-pval)

pval = stats.norm.sf(abs(test_stat))
print(pval)

#%% Question 4.1

coindat = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/coins_collection.csv")

n = coindat.sample(50)
print(n)

s = np.std(n)
print(s)

#%% 4.2
#To take a random sample,
#random.choices() needs an Series, not data frame
ages = coindat['Age']
#We also need a blank set of values to place sds.
samp_sds = [0]*100
i = 0

#%%
#Strategy 1: Repeatedly run this entire cell
#until you get an error. Make sure to run the previous cells first!
sample = random.choices(ages, k = 62)
samp_sds[i] = np.std(sample, ddof =1)
print(samp_sds)
i = i+1

#%%
#Here is another version using "for loops".
#You can run the code in this cell just one time (run entire cell)
# Make sure to run the first two cells first!
for i in range(0,110):
    sample = random.choices(ages, k = 62)
    samp_sds[i] = np.std(sample, ddof =1)

#%% 4.2 Continued

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.distplot(samp_sds, bins=10, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of 100 sample std")
plt.ylabel("Frequency")
plt.xlabel("Age")

#%% 4.4

sigma = coindat['Age'].std()
print(sigma)

meansds = np.mean(samp_sds)
print(meansds)




