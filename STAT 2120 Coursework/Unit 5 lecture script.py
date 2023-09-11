"""""""""""""""""""""""""""""""""""""""

Unit 5 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import scipy.stats as stats
import numpy as np


# Define the Binomial distribution
n = 140
p = 0.08


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that exactly 
5 of the men in the sample are color 
blind?
"""""""""""""""""""""""""""""""""""""""
# Define the number of successes
k = 5

P1 = stats.binom.pmf(k, n, p)

print(P1)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that at most 
5 of the men in the sample are color 
blind?
"""""""""""""""""""""""""""""""""""""""
#P( K <= 5)
P2 = stats.binom.cdf(k, n, p)
P2 = round(P2, 4)
print(P2)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the mean and standard deviation
for the number of color blind men in 
the sample?
"""""""""""""""""""""""""""""""""""""""
mu_b = n*p
print(mu_b)

sigma_b = np.sqrt(n*p*(1-p))
print(sigma_b)


#%%
# Define the Poisson distribution
mu_p = 7


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability of 6 accidents
next month?
"""""""""""""""""""""""""""""""""""""""
# Define the number of successes
k = 6

P3 = stats.poisson.pmf(k, mu_p)
P3 = round(P3, 4)
print(P3)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability of less than
6 accidents next month?
"""""""""""""""""""""""""""""""""""""""
#P(X < 6) = P(X <= 5)
P4 = stats.poisson.cdf(k-1, mu_p)
P4 = round(P4, 4)
print(P4)



#%%
# Define the scaled Poisson distribution
mu_p = 7*12


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability of 75 or fewer
accidents next year?
"""""""""""""""""""""""""""""""""""""""
# Define the number of successes
k = 75

P5 = stats.poisson.cdf(k, mu_p)
P5 = round(P5, 4)
print(P5)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability of between 75
and 90 accidents next year (inclusive)?
"""""""""""""""""""""""""""""""""""""""
# Define the number of successes
k1 = 75
k2 = 90
#P(X < = 90) - P(x <= 74)
P6 = stats.poisson.cdf(k2, mu_p) - stats.poisson.cdf(k1-1, mu_p)
P6 = round(P6, 4)
print(P6)
