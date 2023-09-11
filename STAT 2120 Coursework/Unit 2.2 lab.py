"""""""""""""""""""""""""""""""""""

Unit 2.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import statsmodels.api as sm

# Read in the data; Remember to fix the "backward observation"
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/Crocs.csv"
crocs = pd.read_csv(filename)

#%%
# Define the explanatory and response variables
X = crocs['HeadLength']
X = sm.add_constant(X)
y = crocs['BodyLength']

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Determine the regression equation
model_est = model.params
print(model_est)

b0 = round(model_est[0], 4)
b1 = round(model_est[1], 4)

print("The intercept of the estimated equation is " + str(b0) )
print("The slope of the estimated equation is "  + str(b1) )

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")


#%%
# Determine the coefficient of determination
r2 = model.rsquared
r2 = round(r2,4)
print("The coefficient of determination is " + str(r2) + ".")

#%%
# Determine the predicted Body length for sarchosuchus imperator (160 cm head length)
print(-8.9463 + 6.9494*160)

#%%
# Determine the residual for the first crocodile. 
resid_first = model.resid[0]
print(resid_first)

model.resid

# Check
predict_first = -8.9463 + 6.9494*24
actual_first = 161

residual = actual_first - predict_first
print(residual)







