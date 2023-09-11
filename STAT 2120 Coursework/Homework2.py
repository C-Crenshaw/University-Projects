
# Import needed packages
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

"""""""""""

Question 1

"""""""""""

# Read in data
fastfood = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/fastfood.csv")

#%%
# Fast food scatterplot
sns.scatterplot(x="Restaurants", y="Obesity", data=fastfood)
plt.title("Fast Food Availability and Obesity within the U.S. by State", fontsize = 20)
plt.ylabel("Rate of Obesity (in percentage)", fontsize = 14)
plt.xlabel("Fast Food Restaurants (per capita)", fontsize = 14)

#%%
# Correlation
corr = fastfood.corr()

# Subset and round the correlation coefficient (printing correlation value)
r = corr.iloc[0,1]
r = round(r,3)
print("The correlation between these variables is " + str(r) + ".")


# Least Squares Regression
# Define the explanatory and response variables
X = fastfood["Restaurants"]
X = sm.add_constant(X)  # Adds const column, makes sure a intercept is present in the model (intercept that is not zero)
y = fastfood["Obesity"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Determine the b0 and b1 values (slope and intercept)
model_est = model.params
print(model_est)

#%%
# Determine the regression equation
b0 = round(model_est[0], 3)
b1 = round(model_est[1], 3)

print("The intercept of the estimated equation is " + str(b0) )
print("The slope of the estimated equation is "  + str(b1) )
print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")

# Predict Virginia and find residual
print(22.4026 + 1.8995*4.3)

iVA = fastfood.State == 'Virginia'

yhat_VA = model.fittedvalues[iVA]
yhat_VA = round(yhat_VA,1)
print(yhat_VA)

resid_VA = model.resid[iVA]
resid_VA = round(resid_VA,1)
print(resid_VA)

# Check
predict_first = 22.4026 + 1.8995*4.3
actual_first = 29

residual = actual_first - predict_first
print(residual)

# Coefficient of Determination
r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

#%%
"""""""""""

Question 4

"""""""""""

# Re-create table
# Table values for 2x3 table
procrast_data = {'Sophomore': [120,302],
            'Junior': [381,512],
            'Senior': [88,141]}
procrast = pd.DataFrame(procrast_data, 
                   columns=['Sophomore','Junior','Senior'], 
                   index=['Monday to Saturday','Sunday'])

procrast.loc['All']= procrast.sum(axis=0)
procrast.loc[:,'All'] = procrast.sum(axis=1)

print(procrast)

# Display marginal distribution in percentages
procrast_prop = procrast/procrast.loc["All","All"]
procrast_prop = round(procrast_prop*100,1)
print(procrast_prop)

# Display conditional distribution of the day in percentages
procrast_cond_op = procrast.div(procrast["All"], axis=0)
procrast_cond_op = round(procrast_cond_op*100, 1)
print(procrast_cond_op)

# Display conditional distribution of the academic level
AL = procrast/procrast.loc["All",]
AL = round(AL*100, 1)
print(AL)




