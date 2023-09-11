"""""""""""""""""""""""""""""""""""""""

Unit 10.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

# Read in data
tuition = pd.read_csv(r"C:\Users\rr3pp\Box\stat2120\Rich\Spring 2021\Course materials\Data\tuition.csv")

#%%
"""""""""""""""""""""""""""""""""""""""
Linear regression
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = tuition["Y2008"]
X = sm.add_constant(X)
y = tuition["Y2013"]

# Apply the regression equation
model = sm.OLS(y, X).fit()


#%%
# Specify value for prediction
Xnew = pd.DataFrame([[1, 9000]])

# Predict for that value
pred_new = model.predict(Xnew)
print(pred_new)

#%%
# Determine the confidence interval and prediction interval 
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)


#%%
# Verify the confidence interval
tstar = stats.t.ppf(0.975,31)
LB = 10332.1295 - tstar*286.4786
UB = 10332.1295 + tstar*286.4786

print(LB)
print(UB)


#%%
# ANOVA F test
model_output = model.summary()
print(model_output)


#%%
# ANOVA table components
Total_SS = model.centered_tss
Reg_SS = model.ess
Resid_SS = model.ssr

Total_df = model.nobs - 1
Reg_df = 1
Resid_df = model.nobs - 2

Total_MS = model.mse_total
Reg_MS = model.mse_model
Resid_MS = model.mse_resid

F = model.fvalue
pval = model.f_pvalue



#%%
anova_tbl = pd.DataFrame(columns=['SS','df','MS','F','pvalue'])
anova_tbl.SS = [Reg_SS, Resid_SS, Total_SS]
anova_tbl.df = [Reg_df, Resid_df, Total_df]
anova_tbl.MS = [Reg_MS, Resid_MS, np.nan]
anova_tbl.F = [F, np.nan, np.nan]
anova_tbl.pvalue = [pval, np.nan, np.nan]
anova_tbl.index = ['Regression','Residual','Total']

with pd.option_context('display.max_columns', None):  
    print(anova_tbl)





#%%
"""""""""""""""""""""""""""""""""""""""

Unit 10.2 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tuition = pd.read_csv(r"C:\Users\rr3pp\Box\stat2120\Rich\Spring 2021\Course materials\Data\tuition.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplot with regression line
"""""""""""""""""""""""""""""""""""""""
sns.regplot(x="Y2008", y="Y2013", data=tuition, ci=95)
plt.title("In-state tuition for 2008 and 2013")
plt.ylabel("In-state tuition for 2013")
plt.xlabel("In-state tuition for 2008")
plt.xlim(0, 16000)
plt.ylim(0, 18000)



