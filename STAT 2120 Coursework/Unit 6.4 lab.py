
import numpy as np
import pandas as pd
import scipy.stats as stats

#%% Confidence Interval
sample = [31, 31, 43, 36, 23, 34, 32, 30, 20, 24]
np.mean(sample)

# 95% Confidence Interval
sigma = 7
n = 100
xbar = 30.4

# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

# Determine confidence interval (lower limit and upper limit)
LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(LL)
print(UL)

#%% Hypothesis Test
sigma = 7
n = 100

# Null hypothesis
mu0 = 25

# Test statistic
xbar = 30.4
test_stat = (xbar - mu0)/(sigma/np.sqrt(n))
print(test_stat)

# p-value; test is two-sided, need to double one of the tails
pval = stats.norm.cdf(-abs(test_stat))*2
print(pval)
