"""""""""""""""""""""""""""""""""""

Unit 8.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/personality.csv"
per_data = pd.read_csv(filename)


#%%
# Create the two-way table by filling in the XXX with appropriate column names
per_tbl = pd.crosstab(index=per_data.Study, columns=per_data.Personality)

#%%
#  Sample and known values
n1 = 229
n2 = 224
X1 = 59
X2 = 91
phat1 = X1/n1
phat2 = X2/n2
phat = (X1 + X2)/(n1 + n2)  

# Test statistic
test_stat = (phat1 - phat2)/np.sqrt(phat*(1-phat)*(1/n1 + 1/n2))
print(test_stat)

# p-value; test is two-tailed
pval = 2 * stats.norm.cdf(-abs(test_stat))
print(pval)

#%% Reliable Test

n1*(np.sqrt(phat*(1-phat)*(1/n1 + 1/n2)))

n1*(1-(np.sqrt(phat*(1-phat)*(1/n1 + 1/n2))))

n2*(np.sqrt(phat*(1-phat)*(1/n1 + 1/n2)))

n2*(1-(np.sqrt(phat*(1-phat)*(1/n1 + 1/n2))))

#%%
# Determine z*
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

# Determine confidence interval
LL = (phat1 - phat2) - z_star * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)
UL = (phat1 - phat2) + z_star * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)

print(round(LL,3))
print(round(UL,3))

n1*(np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2))

n1*(1-(np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)))

n2*(np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2))

n2*(1-(np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)))

#%%
# Not including the Prefer not to answer
n = n1 + n2
print(n)

X = X1 + X2
print(X)

p_hat = X/n
print(p_hat)

LL = p_hat - z_star * np.sqrt(p_hat*(1-p_hat)/n)
UL = p_hat + z_star * np.sqrt(p_hat*(1-p_hat)/n)

print(LL)
print(UL)

# All students
N = 478
x = sum(per_data.Study == "Group")
print(x)

P_hat = x/N

LL2 = P_hat - z_star * np.sqrt(P_hat*(1-P_hat)/N)
UL2 = P_hat + z_star * np.sqrt(P_hat*(1-P_hat)/N)

print(LL2)
print(UL2)

n*p_hat

n*(1-p_hat)
