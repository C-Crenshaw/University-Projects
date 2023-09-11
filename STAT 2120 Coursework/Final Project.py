
# Load relevant packages
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fuelecon = pd.read_csv("/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/FuelEconomy_Data.csv")

# Clean dataset of all entries that are not numeric values
fuelecon = fuelecon.dropna()
fuelecon.drop(fuelecon.index[fuelecon['acceleration'] == ']'], inplace=True)
fuelecon.drop(fuelecon.index[fuelecon['horsepower'] == '?'], inplace=True)

# Create a new dataframe to isolate the appropriate explanatory variables
explan = pd.DataFrame(fuelecon[["displacement", "horsepower", "weight", "mpg"]])

# Convert the Horsepower  values to numeric values (solution to error)
explan['horsepower'] = explan['horsepower'].astype(float)

#%% Displacement

# Simple Linear Regression Graph
sns.regplot(x="displacement" , y="mpg" , data=explan, ci=0)
plt.title("Displacement and Fuel Economy of Vehicles")
plt.ylabel("Fuel Economy (MPG)")
plt.xlabel("Displacement (L)")
plt.xlim(50,475)
plt.ylim(5, 45)

#Linear Regression
X = explan["displacement"]
X = sm.add_constant(X)
print(X)
y = explan["mpg"]

model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
print(b0)
b1 = round(model.params[1], 2)
print(b1)

print("The regression equation is: y = " + str(b0) + "+" + str(b1) + "x.")

# Summary Statistic
model_output = model.summary()
print(model_output)

# Residual Plot
# Define the explanatory and response variables
X = explan["displacement"]
X = sm.add_constant(X)
y = explan["mpg"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=explan.displacement, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("Displacement for Vehicles (L)")


#%% Weight

# Simple Linear Regression Graph
sns.regplot(x="weight" , y="mpg" , data=explan, ci=0)
plt.title("Weight and Fuel Economy of Vehicles")
plt.ylabel("Fuel Economy (MPG)")
plt.xlabel("Weight (lb)")
plt.xlim(1500,5250)
plt.ylim(0, 50)

#Linear Regression
X = explan["weight"]
X = sm.add_constant(X)
print(X)
y = explan["mpg"]

model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
print(b0)
b1 = round(model.params[1], 2)
print(b1)

print("The regression equation is: y = " + str(b0) + "+" + str(b1) + "x.")

# Residual Plot
# Define the explanatory and response variables
X = explan["weight"]
X = sm.add_constant(X)
y = explan["mpg"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=explan.weight, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("Weight of Vehicles (lb)")

# Summary Statistic
model_output = model.summary()
print(model_output)

#%% Horsepower

# Simple Linear Regression Graph
sns.regplot(x="horsepower" , y="mpg" , data=explan, ci=0)
plt.title("Horsepower and Fuel Economy of Vehicles")
plt.ylabel("Fuel Economy (MPG)")
plt.xlabel("Horsepower (hp)")

#Linear Regression
X = explan["horsepower"]
X = sm.add_constant(X)
print(X)
y = explan["mpg"]

model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
print(b0)
b1 = round(model.params[1], 2)
print(b1)

print("The regression equation is: y = " + str(b0) + "+" + str(b1) + "x.")

# Summary Statistic
model_output = model.summary()
print(model_output)

# Residual Plot
# Define the explanatory and response variables
X = explan["horsepower"]
X = sm.add_constant(X)
y = explan["mpg"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=explan.horsepower, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("Horsepower of Vehicles (hp)")

#%% Predicting Values for Weight

#Linear Regression
X = explan["weight"]
X = sm.add_constant(X)
print(X)
y = explan["mpg"]

model = sm.OLS(y, X).fit()

# Prediction Value #1
Xnew = pd.DataFrame([[1, 3139]])

# Predict for that value
pred_new = model.predict(Xnew)
print(pred_new)

# Determine the confidence interval and prediction interval 
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)

# Prediction Value #2
Xnew2 = pd.DataFrame([[1, 3278]])

# Predict for that value
pred_new2 = model.predict(Xnew2)
print(pred_new2)

# Determine the confidence interval and prediction interval 
pred2 = model.get_prediction(Xnew2)
CI_PI2 = pred2.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI2)

# Prediction Value #3
Xnew3 = pd.DataFrame([[1, 1795]])

# Predict for that value
pred_new3 = model.predict(Xnew3)
print(pred_new3)

# Determine the confidence interval and prediction interval 
pred3 = model.get_prediction(Xnew3)
CI_PI3 = pred3.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI3)

#%% Multiple Linear Regression

# Define the explanatory and response variables
X = explan[["weight", "displacement", "horsepower"]]
X = sm.add_constant(X)
y = explan["mpg"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Determine the regression equation estimates
bj = round(model.params,3)
print(bj)

model_output = model.summary()
print(model_output)

# Residual Graphs

# Store the residuals and predicted values
m_resid = model.resid
m_pred = model.fittedvalues

# Create plot 1
sns.residplot(x=m_pred, y=m_resid)
plt.title("Residual plot (predicted)")
plt.ylabel("Residuals")
plt.xlabel("Predicted values")

# Create plot 2
sns.residplot(x=explan.weight, y=m_resid)
plt.title("Residual plot (weight of the vehicles)")
plt.ylabel("Residuals")
plt.xlabel("Weight")

# Create plot 3
sns.residplot(x=explan.displacement, y=m_resid)
plt.title("Residual plot (displacement of vehicles)")
plt.ylabel("Residuals")
plt.xlabel("Displacement")

# Create plot 4
sns.residplot(x=explan.horsepower, y=m_resid)
plt.title("Residual plot (horsepower of vehicles)")
plt.ylabel("Residuals")
plt.xlabel("Horsepower")

# T-Test for Slope
model_output = model.summary()
print(model_output)

# Correlation matrix
exp_var = explan[["weight", "displacement", "horsepower"]]
corr = exp_var.corr()
print(corr)

#%% ANOVA F Test
model_output = model.summary()
print(model_output)

#%% Partial F Test

# Original Model (SLR of Weight)
X = explan["weight"]
X = sm.add_constant(X)
print(X)
y = explan["mpg"]

model = sm.OLS(y, X).fit()

# Extended Model
X_ext = explan[["weight", "displacement", "horsepower"]]
X_ext = sm.add_constant(X_ext)
y = explan["mpg"]

# Apply the regression equation
model_ext = sm.OLS(y, X_ext).fit()

# Partial F test
r2_2 = model.rsquared
r2_1 = model_ext.rsquared
 
p = 3
q = 2
n = model.nobs

# Test statistic
test_stat = ( (n-p-1) / q )*( (r2_1-r2_2) / (1-r2_1) )
test_stat = round(test_stat, 2)
print(test_stat)

# p-value
pval = 1 - stats.f.cdf(test_stat, q, n-p-1)
pval = round(pval, 4)
print(pval)

# Adjusted R-squared values
adj_r2 = model.rsquared_adj
adj_r2 = round(adj_r2, 3)
print(adj_r2)

# Adjusted R-squared: extended
adj_r2_ext = model_ext.rsquared_adj
adj_r2_ext = round(adj_r2_ext, 3)
print(adj_r2_ext)

#%% Predicted Values
# Define the explanatory and response variables
X = explan[["weight", "displacement", "horsepower"]]
X = sm.add_constant(X)
y = explan["mpg"]

# Apply the regression equation
model = sm.OLS(y, X).fit()


# Prediction 1
Xnew = pd.DataFrame([[1, 3139, 250, 88]])

# Predict for that value
pred_new = model.predict(Xnew)
print(pred_new)

# prediction interval
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)

# Prediction 2
Xnew = pd.DataFrame([[1, 3278, 250, 100]])

# Predict for that value
pred_new = model.predict(Xnew)
print(pred_new)

# prediction interval
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)

# Prediction 3
Xnew = pd.DataFrame([[1, 1795, 91, 53]])

# Predict for that value
pred_new = model.predict(Xnew)
print(pred_new)

# prediction interval
pred = model.get_prediction(Xnew)
CI_PI = pred.summary_frame()
with pd.option_context('display.max_columns', None):  
    print(CI_PI)

# Check Predicted Values
bj = model.params
print(bj)

y1 = 39.439635 - (0.004841*3139) - (0.005039*250) - (0.021417*88)
print(y1)

y2 = 39.439635 - (0.004841*3278) - (0.005039*250) - (0.021417*100)
print(y2)

y3 = 39.439635 - (0.004841*1795) - (0.005039*91) - (0.021417*53)
print(y3)



