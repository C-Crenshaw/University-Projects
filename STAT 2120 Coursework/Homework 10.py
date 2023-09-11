
# Import needed packages
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#%% Question 1
# Read in data
ozark = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/ozark.csv")

# Scatterplots
sns.scatterplot(x="Area", y="IBI", data=ozark)
plt.title("Area of the watershed (square kilometers) and index of biotic integrity (IBI)")

sns.scatterplot(x="Forest", y="IBI", data=ozark)
plt.title("Percent of the watershed area that is forest and index of biotic integrity (IBI)")

#Scatterplots with Regression Line
sns.regplot(x="Area", y="IBI", data=ozark, ci=0)
plt.title("Area of the watershed (square kilometers) and index of biotic integrity (IBI)")
plt.ylabel("IBI")
plt.xlabel("Area")

sns.regplot(x="Forest", y="IBI", data=ozark, ci=0)
plt.title("Percent of the watershed area that is forest and index of biotic integrity (IBI)")
plt.ylabel("IBI")
plt.xlabel("Forest")

# Multiple Linear Regression
# Define the explanatory and response variables
X = ozark[["Area", "Forest"]]
X = sm.add_constant(X)
y = ozark["IBI"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Determine the regression equation estimates
bj = round(model.params,3)
print(bj)

# t-test and confidence interval for the slope
model_output = model.summary()
print(model_output)

#%%
# Residual Plot (MLR model)
# Define the explanatory and response variables
X = ozark[["Area", "Forest"]]
X = sm.add_constant(X)
y = ozark["IBI"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals and predicted values
m_resid = model.resid
m_pred = model.fittedvalues

# Create plot 
sns.residplot(x=m_pred, y=m_resid)
plt.title("Residual plot (predicted)")
plt.ylabel("Residuals")
plt.xlabel("Predicted values")

# Residual Plot (Area variable)
sns.residplot(x=ozark.Area, y=m_resid)
plt.title("Residual plot (average area)")
plt.ylabel("Residuals")
plt.xlabel("Area")

# Residual Plot (Forest variable)
sns.residplot(x=ozark.Forest, y=m_resid)
plt.title("Residual plot (average percentage of forest)")
plt.ylabel("Residuals")
plt.xlabel("Forest")

#%% Significance Test

# ANOVA table components
Total_SS = model.centered_tss
Reg_SS = model.ess
Resid_SS = model.ssr

Total_df = model.nobs - 1
Reg_df = 2
Resid_df = model.nobs - 3

Total_MS = model.mse_total
Reg_MS = model.mse_model
Resid_MS = model.mse_resid

F = model.fvalue
pval = model.f_pvalue

anova_tbl = pd.DataFrame(columns=['SS','df','MS','F','pvalue'])
anova_tbl.SS = [Reg_SS, Resid_SS, Total_SS]
anova_tbl.df = [Reg_df, Resid_df, Total_df]
anova_tbl.MS = [Reg_MS, Resid_MS, np.nan]
anova_tbl.F = [F, np.nan, np.nan]
anova_tbl.pvalue = [pval, np.nan, np.nan]
anova_tbl.index = ['Regression','Residual','Total']

with pd.option_context('display.max_columns', None):  
    print(anova_tbl)

#%% Prediction
# Specify value for a prediction with specified values
Xnew = pd.DataFrame([[1,  55, 84]])

# Predict for that value
pred_new = model.predict(Xnew)
pred_new = round(pred_new, 1)
print(pred_new)

#Prediction and confidence interval
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)

# Confirm Confidence Interval
tstar = stats.t.ppf(0.975,47)
LB = 91.6 - tstar*5.461
UB = 91.6 + tstar*5.461

print(LB)
print(UB)

#%% Question 2

# ANOVA table components
Total_SS = 10332.2
Reg_SS = 2840.4
Resid_SS = 7491.8

Total_df = 79
Reg_df = 2
Resid_df = 77

Reg_MS = 1420.2
Resid_MS = 97.3
Total_MS = Total_SS/79

F = Reg_MS / Resid_MS
print(F)

# Coefficient of Determination
r1 = Reg_SS/Total_SS
print(r1)

r2 = 2986.2/10332.2
print(r2)

# Adjusted R squared 
r1 = 1 - Resid_MS / Total_MS
print(r1)

r2 = 1 - (97.7/(10332.2/79))
print(r2)

#%% Partial F Test

# Partial F test
r2_2 = 0.2749075705077331
r2_1 = 0.28901879560984106
 
p = 4
q = 2
n = 49

# Test statistic
test_stat = ( (n-p-1) / q )*( (r2_1-r2_2) / (1-r2_1) )
print(test_stat)

# p-value
pval = 1 - stats.f.cdf(test_stat, q, n-p-1)
print(pval)






