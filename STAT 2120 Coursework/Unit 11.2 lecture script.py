"""""""""""""""""""""""""""""""""""""""

Unit 11.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

# Read in data
hospital = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/hospital_ext.csv")

#%%
"""""""""""""""""""""""""""""""""""""""
Multiple linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = hospital[["Stay", "Age", "Xray"]]
X = sm.add_constant(X)
y = hospital["Risk"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

#%%
# Regression standard error
s = np.sqrt(model.mse_resid)
s = round(s, 2)
print(s)

#%%
# Coefficient of determination
r2 = model.ess/model.centered_tss
r2 = round(r2, 3)
print(r2)

r2 = model.rsquared
r2 = round(r2, 3)
print(r2)

#%%
# ANOVA F test
model_output = model.summary()
print(model_output)


#%%
"""""""""""""""""""""""""""""""""""""""
Extended multiple linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X_ext = hospital[["Stay", "Age", "Xray", "Nurses", "Beds"]]
X_ext = sm.add_constant(X_ext)
y = hospital["Risk"]

# Apply the regression equation
model_ext = sm.OLS(y, X_ext).fit()


#%%
# Partial F test
r2_2 = model.rsquared
r2_1 = model_ext.rsquared
 
p = 5
q = 2
n = model.nobs

# Test statistic
test_stat = ( (n-p-1) / q )*( (r2_1-r2_2) / (1-r2_1) )
test_stat = round(test_stat, 2)
print(test_stat)

#%%
# p-value
pval = 1 - stats.f.cdf(test_stat, q, n-p-1)
pval = round(pval, 4)
print(pval)


#%%
# Adjusted R-squared
print(model_output)

#%%
# Adjusted R-squared: original
adj_r2 = model.rsquared_adj
adj_r2 = round(adj_r2, 3)
print(adj_r2)

#%%
# Adjusted R-squared: extended
adj_r2_ext = model_ext.rsquared_adj
adj_r2_ext = round(adj_r2_ext, 3)
print(adj_r2_ext)







