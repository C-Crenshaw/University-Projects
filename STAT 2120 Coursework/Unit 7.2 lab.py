import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

stroop_stu = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/stroop_students.csv")
stroop_TAs = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/stroop_ta.csv")


#%% Question 1

# Create the needed data
diff = stroop_stu.Round2 - stroop_stu.Round1

# Known and sample values for students (population 1)
n1 = 334
xbar1 = np.mean(diff)
print(xbar)
s1 = np.std(diff, ddof =1)
print(s)

# Known and sample values for TAs (population 2)
inc = stroop_TAs.Different - stroop_TAs.Same

n2 = 38
xbar2 = np.mean(inc)
print(xbar2)
s2 = np.std(inc, ddof =1)
print(s2)

# Test statistic
test_stat = (xbar1 - xbar2)/(np.sqrt(s1**2/n1 + s2**2/n2))
print(test_stat)
# Step 2: t = 0.285775
#%%
# Degrees of freedom
df_min = np.min([n1-1, n2-1])
print(df_min)

#%%
# p-value; test is two-tailed
pval = stats.t.cdf(-abs(test_stat), df=df_min)*2
print(pval)

#%% Confidence Interval
t_star = stats.t.ppf(0.975, df=df_min)
t_star = round(t_star, 3)
print(t_star)

# student average time to complete first round
xbar3 = np.mean(stroop_stu.Round1)
print(xbar3)
s3 = np.std(stroop_stu.Round1, ddof =1)
print(s3)

# TA average time
xbar4 = np.mean(stroop_TAs.Same)
print(xbar4)
s4 = np.std(stroop_TAs.Same, ddof =1)
print(s4)

# Determine confidence interval
LL = (xbar3 - xbar4) - t_star * np.sqrt(s3**2/n1 + s4**2/n2)
UL = (xbar3 - xbar4) + t_star * np.sqrt(s3**2/n1 + s4**2/n2)

print(LL)
print(UL)

