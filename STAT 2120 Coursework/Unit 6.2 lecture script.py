"""""""""""""""""""""""""""""""""""""""

Unit 6.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import scipy.stats as stats

stats.norm.ppf(0.975)


#%%
"""""""""""""""""""""""""""""""""""""""
Sampling distribution ranges
"""""""""""""""""""""""""""""""""""""""
mu = 65
sigma = 5
n = 12

sigma_xbar = sigma/np.sqrt(n)

LL = mu - 2 * sigma_xbar
UL = mu + 2 * sigma_xbar

print(round(LL,1))
print(round(UL,1))


#%%
"""""""""""""""""""""""""""""""""""""""
95% confidence interval
"""""""""""""""""""""""""""""""""""""""
# Given information
sigma = 12.3
n = 110
xbar = 76.7

# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

#%%
# Determine confidence interval (lower limit and upper limit)
LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))


#%%
"""""""""""""""""""""""""""""""""""""""
95% confidence interval, n=25
"""""""""""""""""""""""""""""""""""""""
n = 25

LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))


#%%
"""""""""""""""""""""""""""""""""""""""
Sample size
"""""""""""""""""""""""""""""""""""""""
m_star = 3

n = (z_star * sigma / m_star)**2
n = np.ceil(n)
print(n)

# Need a sample size of 65 to achieve a margin of error of 3

