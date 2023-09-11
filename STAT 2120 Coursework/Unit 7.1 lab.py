import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

stroop = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/stroop_ta.csv")

# Create the needed data
mean_inc = stroop.Different - stroop.Same

# Known and sample values
n = 38
mu0 = 7.5
xbar = np.mean(mean_inc)
print(xbar)
s = np.std(mean_inc, ddof =1)
print(s)

test_stat = (xbar - mu0)/(s/np.sqrt(n))
print(test_stat)

# p-value; test is right-tailed
pval = 1- stats.t.cdf(test_stat, df=n-1)
print(pval)

pval2 = stats.t.sf(abs(test_stat), df=n-1)
print(pval2)

# Determine t*
t_star = stats.t.ppf(0.95, df=n-1)
t_star = round(t_star, 3)
print(t_star)

# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(LL,1)
print(UL,1)

#%% Histogram

sns.distplot(mean_inc, bins=8, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of of time increase among STAT TAs")
plt.ylabel("Frequency")
plt.xlabel("Time Increase")

histrgram = sns.distplot(mean_inc)

#%% Question 8

n = 38
mu0 = 15

xbar = np.mean(mean_inc)
s = np.std(mean_inc, ddof = 1)  # This is the n-1 argument that must be present in taking the std of a sample

# Test statistic
test_stat = (xbar - mu0)/(s/np.sqrt(n))
print(test_stat)

# p-value; test is left-tailed
pval = 1-stats.t.cdf(test_stat, df=n-1)
print(pval)


# Confirm above conclusion
# Determine t*
t_star = stats.t.ppf(0.95, df=n-1) # must specify degrees of freedom
t_star = round(t_star, 3)
print(t_star)

# Determine confidence interval
LL = xbar - t_star * s/np.sqrt(n)
UL = xbar + t_star * s/np.sqrt(n)

print(round(LL,1))
print(round(UL,1))
