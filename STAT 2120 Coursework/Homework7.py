import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in data
noso = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/nosocomial.csv")

# Create the needed data
diff = noso.Infected - noso.NotInfected

#%%
# Known and sample values
n = 52
xbar = np.mean(diff)
print(xbar)
sigma = 13.5

# Determine confidence interval
z_star = stats.norm.ppf(0.95)
z_star = round(z_star, 3)
print(z_star)

LL = xbar - z_star * sigma/np.sqrt(n)
UL = xbar + z_star * sigma/np.sqrt(n)

print(round(LL,4))
print(round(UL,4))

# Margin of error
MOE = z_star * sigma/np.sqrt(n)
print(MOE)

m_star = .10*11.3846  # 10 percent of the value of the sample statistic
n = (z_star * sigma / m_star)**2
n = np.ceil(n)
print(n)

#%% Hypothesis Test
sigma = 13.5
n = 52

# Null hypothesis
mu0 = 0

test_stat = (xbar - mu0)/(sigma/np.sqrt(n))
print(test_stat)

# p-value; right-tailed
pval = 1 - stats.norm.cdf(test_stat)
print(pval)
