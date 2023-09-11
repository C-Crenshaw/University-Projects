"""""""""""""""""""""""""""""""""""""""

Unit 9 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats

# Read in data
school = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/school.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Two-way tables
"""""""""""""""""""""""""""""""""""""""
# Create the two-way table
tw_tbl = pd.crosstab(index=school.school_type, columns=school.goals,
                            margins=True)
print(tw_tbl)

#%%
# Display joint and marginal proportions 
tw_tbl_prop = tw_tbl/tw_tbl.loc["All","All"] # dividing the entire table by the value in [All, All] or 478
tw_tbl_prop = round(tw_tbl_prop, 4)
print(tw_tbl_prop)

#%%
# Display joint and marginal percentages
tw_tbl_per = tw_tbl_prop * 100
print(tw_tbl_per)

#%%
# Display conditional proportions
tw_tbl_cond = tw_tbl.div(tw_tbl["All"], axis=0)
tw_tbl_cond = round(tw_tbl_cond, 4)
print(tw_tbl_cond)

#%%
# Display conditional percentages
tw_tbl_cond_per = tw_tbl_cond * 100
print(tw_tbl_cond_per)


#%%
"""""""""""""""""""""""""""""""""""""""
Chi-square test
"""""""""""""""""""""""""""""""""""""""
# Determine expected counts
ct = tw_tbl.All[0:3]                            # Isolates column totals
rt = tw_tbl.loc["All"][0:3]                     # Isolates row totals
rtimesc = np.outer(ct,rt)                       # Multiplies the column and row totals appropriately
exp = rtimesc/tw_tbl.loc["All","All"]           # Divides all column and row total products by the sample size
exp = np.round(exp, 2)                          # Rounds the expected counts
exp = pd.DataFrame(exp)                         # Creates a DataFrame
exp.columns = ["Grades","Popular","Sports"]     # Names the DataFrame columns
exp.index = ["Rural","Suburban","Urban"]        # Names the DataFrame rows
print(exp)


#%%
# Isolate the observed counts from the two-way table
obs = tw_tbl.iloc[0:3,0:3]
print(obs)

#%%
# Determine test statistic components
test_stat_all = (obs - exp)**2 / exp
print(test_stat_all)

#%%
# Determine test statistic
test_stat = np.sum(test_stat_all).sum()
test_stat = round(test_stat, 2)
print(test_stat)

#%%
# Determine p-value
pval = 1 - stats.chi2.cdf(test_stat, df=4)
pval = round(pval, 4)
print(pval)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 9 graphics

"""""""""""""""""""""""""""""""""""""""

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read in data
school = pd.read_csv("C:\Users\rr3pp\Box\stat2120\Rich\Spring 2021\Course materials\Data\school.csv")

#%%
# With counts
sns.countplot(x="school_type", hue="goals", data=school)

#%% 
# With joint proportions
sns.barplot(x="school_type", hue="goals", data=school, y="school_type", orient="v", estimator=lambda x: len(x)/len(school))
plt.ylabel("Proportion")

