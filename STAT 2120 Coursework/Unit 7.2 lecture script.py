"""""""""""""""""""""""""""""""""""""""

Unit 7.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in data
jumps_copy = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/jumps_copy.csv")
jumps_con = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/jumps_construction.csv")

#%%
#Step 1:
 
#H_0 : mu_copy - mu_con = 0
#H_A :  mu_copy - mu_con < 0
    

#%%
"""""""""""""""""""""""""""""""""""""""
Frog jumps
"""""""""""""""""""""""""""""""""""""""
# Known and sample values for copy paper frogs (population 1)
n1 = 105
xbar1 = np.mean(jumps_copy.distance)
s1 = np.std(jumps_copy.distance, ddof = 1)

# Known and sample values for construction paper frogs (population 2)
n2 = 126
xbar2 = np.mean(jumps_con.distance)
s2 = np.std(jumps_con.distance, ddof = 1)


# Test statistic
test_stat = (xbar1 - xbar2)/(np.sqrt(s1**2/n1 + s2**2/n2))
print(test_stat)
# Step 2: t = -3.99
#%%
# Degrees of freedom
df_min = np.min([n1-1, n2-1])
print(df_min)

#%%
# p-value; test is left-tailed
pval = stats.t.cdf(test_stat, df=df_min)
print(pval)
#Step 3: P = .0000609
#Step 4: P < alpha (for any reasonable test), REJECT H_0
#Step 5: Based on our 231 data points, we have sufficient 
#evidence to suggest that construction paper frogs jump further, on average,
# than copy paper frogs. If you want a frog to jump further, then make it 
#out of construction paper!
#%%
# Determine t*
t_star = stats.t.ppf(0.975, df=df_min)
t_star = round(t_star, 3)
print(t_star)

#%%
# Determine confidence interval
LL = (xbar1 - xbar2) - t_star * np.sqrt(s1**2/n1 + s2**2/n2)
UL = (xbar1 - xbar2) + t_star * np.sqrt(s1**2/n1 + s2**2/n2)

print(round(LL,1))
print(round(UL,1))

# Conclusion: We are 95% confident that the true difference in average 
# jumping distance between copy paper and construction paper frogs is 
# between 6.5 and 2.2 cm, with construction paper frogs jumping further. 
# Lesson: Construction paper frogs jump further.


nd construction paper frogs is 
# between 6.5 and 2.2 cm, with construction paper frogs jumping further. 
# Lesson: Construction paper frogs jump further.


