# Import needed packages
import scipy.stats as stats
import numpy as np

# Define the Poisson distribution
mu_p = 14.75

# 29 shark attacks
k = 29

P3 = stats.poisson.pmf(k, mu_p)
P3 = round(P3, 4)
print(P3)

# At least 29
P4 = stats.poisson.cdf(k-1, mu_p)
P4 = round(P4, 4)
print(1-P4)

#%%
# Quiz Question
n = 10
p = 0.20

P2 = stats.binom.cdf(1, n, p)
P2 = round(P2, 4)
print(P2)


P1 = stats.binom.cdf(3, n, p)
P1 = round(P1, 4)
print(1-P1)

mu_b = n*p
print(mu_b)

sigma_b = np.sqrt(n*p*(1-p))
print(sigma_b)
