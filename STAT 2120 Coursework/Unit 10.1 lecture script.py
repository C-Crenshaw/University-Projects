"""""""""""""""""""""""""""""""""""""""

Unit 10.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

# Read in data
tuition = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/tuition.csv")

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
# Determine the regression equation
b0 = round(model.params[0], 2)
print(b0)
b1 = round(model.params[1], 2)
print(b1)

print("The regression equation is: y = " + str(b0) + " + " + str(b1) + "x.")

#%%
# Determine the row for UVa
i = tuition.University == 'Virginia'

# Determine the residual for UVa
resid_VA = model.resid[i]
resid_VA = round(resid_VA, 2)
print(resid_VA)
#Since residuals are observed - fitted, this means that 
#UVA tuition in 2013 is about $1000 cheaper than the regression model predicts
# using these data
#%%
# t-test and confidence interval for the slope
model_output = model.summary()
print(model_output)



#%%
# Verify the test statistic
test_stat = .9522/0.116
print(test_stat)

# Verify the p-value
pval = (1-stats.t.cdf(8.231,31))*2
print(pval)

#%%
# Verify the confidence interval
tstar = stats.t.ppf(0.975,31)
LB = 0.9522 - tstar*0.116
UB = 0.9522 + tstar*0.116

print(LB)
print(UB)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 10.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tuition = pd.read_csv(r"C:\Users\rr3pp\Box\stat2120\Rich\Spring 2021\Course materials\Data\tuition.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplot with regression line
"""""""""""""""""""""""""""""""""""""""
sns.regplot(x="Y2008", y="Y2013", data=tuition, ci=0)
plt.title("In-state tuition for 2008 and 2013")
plt.ylabel("In-state tuition for 2013")
plt.xlabel("In-state tuition for 2008")
plt.xlim(0, 16000)
plt.ylim(0, 18000)


#%%
"""""""""""""""""""""""""""""""""""""""
Create residual plot 
"""""""""""""""""""""""""""""""""""""""
# Define the explanatory and response variables
X = tuition["Y2008"]
X = sm.add_constant(X)
y = tuition["Y2013"]

# Apply the regression equation
model = sm.OLS(y, X).fit()

# Store the residuals
m_resid = model.resid

# Create plot 
sns.residplot(x=tuition.Y2008, y=m_resid)
plt.title("Residual plot")
plt.ylabel("Residuals")
plt.xlabel("In-state tuition for 2008")




