"""""""""""""""""""""""""""""""""""""""

Unit 11.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import pandas as pd
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
# Determine the regression equation estimates
bj = round(model.params,3)
print(bj)

#%%
# Predicted value for the observation in index 0
yhat = model.fittedvalues[0]
yhat = round(yhat,1)
print(yhat)

#%%
# Specify value for a prediction with specified values
Xnew = pd.DataFrame([[1,  7.13, 55.7, 39.6]])

# Predict for that value
pred_new = model.predict(Xnew)
pred_new = round(pred_new, 1)
print(pred_new)

#%%
# t-test and confidence interval for the slope
model_output = model.summary()
print(model_output)



#%%
############
# SLR
############
# Define the explanatory and response variables
X2 = hospital["Age"]
X2 = sm.add_constant(X2)
y = hospital["Risk"]

# Apply the regression equation
model2 = sm.OLS(y, X2).fit()

# t-test for slope
model2_output = model2.summary()
print(model2_output)


#%%
# Correlation matrix
exp_var = hospital[["Stay", "Age", "Xray"]]
corr = exp_var.corr()
print(corr)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 11.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

hospital = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/hospital_ext.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplots
"""""""""""""""""""""""""""""""""""""""
sns.scatterplot(x="Stay", y="Risk", data=hospital)
plt.title("Infection risk and average length of stay")

#%%
sns.scatterplot(x="Age", y="Risk", data=hospital)
plt.title("Infection risk and average patient age")

#%%
sns.scatterplot(x="Xray", y="Risk", data=hospital)
plt.title("Infection risk and number of x-rays given")



#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plots 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = hospital[["Stay", "Age", "Xray"]]
X = sm.add_constant(X)
y = hospital["Risk"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals and predicted values
m_resid = model.resid
m_pred = model.fittedvalues

#%%
# Create plot 
sns.residplot(x=m_pred, y=m_resid)
plt.title("Residual plot (predicted)")
plt.ylabel("Residuals")
plt.xlabel("Predicted values")

#%%
# Create plot 
sns.residplot(x=hospital.Stay, y=m_resid)
plt.title("Residual plot (average length of stay)")
plt.ylabel("Residuals")
plt.xlabel("Stay")

#%%
# Create plot 
sns.residplot(x=hospital.Age, y=m_resid)
plt.title("Residual plot (average age of patient)")
plt.ylabel("Residuals")
plt.xlabel("Age")

#%%
# Create plot 
sns.residplot(x=hospital.Xray, y=m_resid)
plt.title("Residual plot (number of xrays)")
plt.ylabel("Residuals")
plt.xlabel("Xray")




