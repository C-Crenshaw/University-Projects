
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in data
hel = pd.read_csv("/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/helium.csv")

#%% Question 1

# Known values
n = 39*2

# Null hypothesis
mu0 = 20

#  Sample values
xbar = np.mean(hel.Distance)
s = np.std(hel.Distance, ddof = 1)  # This is the n-1 argument that must be present in taking the std of a sample

# Test statistic
test_stat = (xbar - mu0)/(s/np.sqrt(n))
print(test_stat)

# p-value; test is right-tailed
pval = 1-stats.t.cdf(test_stat, df=n-1)
print(pval)

t_star = stats.t.ppf(0.975, df=n-1) # must specify degrees of freedom
t_star = round(t_star, 3)
print(t_star)

# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))

print(t_star * s/np.sqrt(n))

#%% Question 2

air = hel[hel.Fill == 'air']
helium = hel[hel.Fill == 'helium']


# Known and sample values for standard air balls (population 1)
n1 = 39
xbar1 = np.mean(air.Distance)
s1 = np.std(air.Distance, ddof = 1)

# Known and sample values for helium balls (population 2)
n2 = 39
xbar2 = np.mean(helium.Distance)
s2 = np.std(helium.Distance, ddof = 1)


# Test statistic
test_stat = (xbar1 - xbar2)/(np.sqrt(s1**2/n1 + s2**2/n2))
print(test_stat)

# Degrees of freedom
df_min = np.min([n1-1, n2-1])
print(df_min)

# p-value; test is left-tailed
pval1 = stats.t.cdf(test_stat, df=df_min)
print(pval1)

t_star = stats.t.ppf(0.975, df=df_min)
t_star = round(t_star, 3)
print(t_star)

# Determine confidence interval
LL = (xbar1 - xbar2) - t_star * np.sqrt(s1**2/n1 + s2**2/n2)
UL = (xbar1 - xbar2) + t_star * np.sqrt(s1**2/n1 + s2**2/n2)

print(round(LL,1))
print(round(UL,1))

print(t_star * np.sqrt(s1**2/n1 + s2**2/n2))


pval2 = stats.t.cdf(-abs(1.026), df=3)*2
print(pval2)

