"""
Created on Thu Oct 28 00:49:55 2021

@author: statr
"""
import pandas as pd
import numpy as np

filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/AreYouWinning.csv"

labdat = pd.read_csv(filename)

mysamp = labdat.sample(n=15)

my_x = sum(mysamp.Response == "Losing more often than winning")
print(my_x)

my_n = 15
p_hat = my_x/my_n
print(p_hat)

p0 = 0.371

# Test statistic
test_stat = (p_hat - p0)/np.sqrt(p0*(1-p0)/my_n)
print(test_stat)
#Step 2: z = 2.90497

# p-value; test is two-tailed
pval = stats.norm.cdf(-abs(test_stat))*2
print(pval)
#Step 3: P = 0.003673  (Really small)
#Step 4: Since P< alpha, Reject H_0. 
#Step 5: Based on the data provided, we have sufficient evidence to suggest that the percentage of Americans who feel their side is losing more often than winning is not 37.1%

my_n*(1-p0)

my_n*p0 

#%% Confidence Interval
z_star = stats.norm.ppf(0.975)
z_star = round(z_star, 3)
print(z_star)

# Determine confidence interval
LL = p_hat - z_star * np.sqrt(p_hat*(1-p_hat)/my_n)
UL = p_hat + z_star * np.sqrt(p_hat*(1-p_hat)/my_n)

print(round(LL,3))
print(round(UL,3))

#Conclusion: We are 95% confident that the true proportion of people who feel that their side is losing more often than winning is 0.51 to 0.957. 

my_n*p_hat
my_n*(1-p_hat)

#%% Margin of Error

m_star = 0.01
p_star = p_hat # proportion of “losing more than winning” responses as an educated guess

n = (z_star / m_star)**2 * p_star*(1-p_star)
n = np.ceil(n)
print(n)




