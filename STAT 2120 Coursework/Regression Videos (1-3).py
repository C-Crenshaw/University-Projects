#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:22:47 2022

@author: CarsonCrenshaw
"""

import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

croc = pd.read_csv("/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/Crocs.csv")

#%% Video 1

sns.regplot(x="HeadLength" , y="BodyLength" , data=croc, ci=0)
plt.title("Head and Body Length of Crocs")
plt.ylabel("Body Length (cm)")
plt.xlabel("Head Length (cm)")
plt.xlim(20,90)
plt.ylim(0, 650)

#Linear Regression
X = croc["HeadLength"]
X = sm.add_constant(X)
print(X)
y = croc["BodyLength"]

model = sm.OLS(y, X).fit()

b0 = round(model.params[0], 2)
b1 = round(model.params[1], 2)

print("The regression equation is: y = " + str(b0) + "+" + str(b1) + "x.")

#%% Video 2

# determine the row for the croc with the head length of 83
i = croc.HeadLength == 83
print(i)

# determine residual for this croc
resid_83 = model.resid[i]
resid_83 = round(resid_83, 2) 
print(resid_83)
# this croc's actual body length is about 20 cm shorter than what the model predicts

# t-test and confidence interval for the slope
model_output = model.summary()
print(model_output)

# const = intercept

#%% Video 3

# Building multiple linear regression models using more than one predictor
share = pd.read_csv("/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/day (1).csv")
print(share)

# varaibles we want are the "feels like" temperature called "atemp" and the average wind speed for the day called "windspeed"
# our response variable is the total count of bike rentals on the given day

X = share[["atemp", "windspeed"]]
X = sm.add_constant(X)
print(X)
y = share["count"]
print(y)

model = sm.OLS(y, X).fit()

bj = round(model.params, 3)
print(bj)

# print the prediction from the first row
yhat = model.fittedvalues[0]
yhat = round(yhat, 1)
print(yhat)

# making a prediction for a future value
Xnew = pd.DataFrame([[1, .474, .1904]])
pred_new = model.predict(Xnew)
pred_new = round(pred_new, 1)
print(pred_new)
# On a day with average windspeed and temp, we would expect a total of 4502 bikes to be rented

# summary of the regression line
model_output = model.summary()
print(model_output)

# r-squred says that the model accounts for about 41% of the variation in the number of bike rentals (not a great measure, better than nothing)


