# Import needed packages
import scipy.stats as stats
import numpy as np

#%% Question 1
# Define the Poisson distribution
mu_p = 224

# More than 50 in 4 weeks
k = 50

P5 = stats.poisson.cdf(k, mu_p)
P5 = round(P5, 4)
print(1-P5)


#%%
# Define the Binomial distribution
n = 10000
p = 0.00005

k = 1

P2 = stats.binom.cdf(k-1, n, p)
P2 = round(P2, 4)
print(1-P2)

#%%
mu_p = 3

# Define the number of successes (more than 4)
k = 4

P3 = stats.poisson.cdf(k, mu_p)
P3 = round(P3, 4)
print(1-P3)

#%%
# Define the Poisson distribution
mu_p = 0.1078

# 2 shark attacks
k = 2

P4 = stats.poisson.pmf(k, mu_p)
P4 = round(P4, 4)
print(P4)

# At least 2
P6 = stats.poisson.cdf(k-1, mu_p)
P6 = round(P6, 4)
print(1-P6)

# Define the Poisson distribution
mu_p2 = 19.67*(1/182)

# 2 shark attacks
k2 = 2

P7 = stats.poisson.pmf(k2-1, mu_p2)
print(1-P7)
