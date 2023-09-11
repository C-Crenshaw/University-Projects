"""""""""""""""""""""""""""""""""""""""

Unit 8.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import scipy.stats as stats

#%%
"""""""""""""""""""""""""""""""""""""""
Venmo
"""""""""""""""""""""""""""""""""""""""
# Null hypothesis
#Step 1: 
#H_0: p = 0.5
#H_a: p >0.5
# alpha = 0.05

p0 = 0.5

#  Sample and known values
n = 52
X = 42
phat = X/n  

# Test statistic
test_stat = (phat - p0)/np.sqrt(p0*(1-p0)/n)
print(test_stat)
#Step 2: z = 4.4376
#%%
# p-value; test is right-tailed
pval = 1 - stats.norm.cdf(test_stat)
print(pval)

#Step 3: P = 0.0000045834  (Really small)
#Step 4: Since P< alpha, Reject H_0. 
#Step 5: Based on the data provided, we have sufficient evidence to suggest
# that people prefer to make friends to pay back in rounded amounts. 
# perhaps: If you want to make more friends, pay back in rounded amounts!

n*(1-p0)

n*p0


#%%
# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

#%%
# Determine confidence interval
LL = phat - z_star * np.sqrt(phat*(1-phat)/n)
UL = phat + z_star * np.sqrt(phat*(1-phat)/n)

print(round(LL,3))
print(round(UL,3))

#Conclusion: We are 95% confident that the true proportion of people who
# prefer a friend who pays back in rounded amounts is between
# 0.701 and 0.915. 
n*phat
n*(1-phat)


#%%
"""""""""""""""""""""""""""""""""""""""
Sample size
"""""""""""""""""""""""""""""""""""""""
m_star = 0.05
p_star = 0.5

n = (z_star / m_star)**2 * p_star*(1-p_star)
n = np.ceil(n)
print(n)
