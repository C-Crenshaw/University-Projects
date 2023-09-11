"""""""""""""""""""""""""""""""""""""""

Unit 7.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in data
jumps = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/jumps_copy.csv")
chol = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/cholesterol_full.csv")

#%%
"""""""""""""""""""""""""""""""""""""""
Frog jumps
"""""""""""""""""""""""""""""""""""""""
# Known values
n = 105

# Null hypothesis
mu0 = 13

#  Sample values
xbar = np.mean(jumps.distance)
s = np.std(jumps.distance, ddof = 1)  # This is the n-1 argument that must be present in taking the std of a sample

# Test statistic
test_stat = (xbar - mu0)/(s/np.sqrt(n))
print(test_stat)

#%%
# p-value; test is left-tailed
pval = stats.t.cdf(test_stat, df=n-1)
print(pval)

# Conclusion: The data do not provide sufficent evidence to state that the mean jump distance for copy paper frogs is less than 13 cm, on average. 


#%%
# Determine t*
t_star = stats.t.ppf(0.975, df=n-1) # must specify degrees of freedom
t_star = round(t_star, 3)
print(t_star)

#%%
# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))

#Conclusion: We are 95% confident that the true mean triple jump distance for copy paper frogs is between 14.0 cm and 16.6 cm. 

#%%
"""""""""""""""""""""""""""""""""""""""
Cholesterol
"""""""""""""""""""""""""""""""""""""""
# Create the needed data
level_red = chol.level_day2 - chol.level_day4

#%%
# Known and sample values
n = 28
xbar = np.mean(level_red)
s = np.std(level_red, ddof =1)

# Determine t*
t_star = stats.t.ppf(0.975, df=n-1)
t_star = round(t_star, 3)
print(t_star)

#%%
# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))
