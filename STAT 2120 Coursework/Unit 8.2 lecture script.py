"""""""""""""""""""""""""""""""""""""""

Unit 8.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import scipy.stats as stats

#%%
"""""""""""""""""""""""""""""""""""""""
First Amendment
"""""""""""""""""""""""""""""""""""""""
#  Sample and known values
n1 = 430
n2 = 516
X1 = 380
X2 = 434

phat1 = X1/n1
print(phat1)
phat2 = X2/n2
print(phat2)
phat = (X1 + X2)/(n1 + n2)  

# Test statistic
test_stat = (phat1 - phat2)/np.sqrt(phat*(1-phat)*(1/n1 + 1/n2))
print(test_stat)

#%%
# p-value; test is two-tailed
pval = 2 * stats.norm.cdf(-abs(test_stat))
print(pval)


#%%
# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

#%%
# Determine confidence interval
LL = (phat1 - phat2) - z_star * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)
UL = (phat1 - phat2) + z_star * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)

print(round(LL,3))
print(round(UL,3))


#%%
"""""""""""""""""""""""""""""""""""""""
Sample size
"""""""""""""""""""""""""""""""""""""""
m_star = 0.10
p_star = 0.5

n = (z_star / m_star)**2 * p_star*(1-p_star) * 2
n = np.ceil(n)
print(n)
