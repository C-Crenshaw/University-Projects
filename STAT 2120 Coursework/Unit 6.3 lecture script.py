"""""""""""""""""""""""""""""""""""""""

Unit 6.3 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import scipy.stats as stats


#%%
"""""""""""""""""""""""""""""""""""""""
Tomatoes
"""""""""""""""""""""""""""""""""""""""
# Known values, Normally distributed
sigma = 5
n = 4

# Null hypothesis
mu0 = 227

# Test statistic
xbar = 222
test_stat = (xbar - mu0)/(sigma/np.sqrt(n))
print(test_stat)

#%%
# p-value; test is two-sided, need to double one of the tails
pval = stats.norm.cdf(-abs(test_stat))*2
print(pval)


#%%
"""""""""""""""""""""""""""""""""""""""
Eggs
"""""""""""""""""""""""""""""""""""""""
# Known values
sigma = 5
n = 12

# Null hypothesis
mu0 = 65

# Test statistic
xbar = 64.2
test_stat2 = (xbar - mu0)/(sigma/np.sqrt(n))
print(test_stat2)

#%%
# p-value; test is one-sided (left tailed)
pval = stats.norm.cdf(test_stat2)
print(pval)

# Not sufficient evidence to suggest that white eggs are lighter than brown
