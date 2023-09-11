"""""""""""""""""""""""""""""""""""""""

Unit 4.3 examples

"""""""""""""""""""""""""""""""""""""""
# Import packages
import numpy as np


# Input the components of the probability distribution
X = np.array([0, 1, 2, 3])
P = np.array([1/8, 3/8, 3/8, 1/8])


#%%
"""""""""""""""""""""""""""""""""""""""
What is the mean number of residents you will meet?
"""""""""""""""""""""""""""""""""""""""
mu_X = np.sum(X * P)
print(mu_X)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the variance of the number of 
VA residents you will meet?
"""""""""""""""""""""""""""""""""""""""
sigma2_X = np.sum((X-mu_X)**2 * P)
print(sigma2_X)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the standard deviation of the 
number of VA residents you will meet?
"""""""""""""""""""""""""""""""""""""""
sigma_X = np.sqrt(sigma2_X)
sigma_X = round(sigma_X, 4)
print(sigma_X)



#%%
# Define investment characteristics
mu_T = 5.0
mu_I = 13.2
sigma_T = 2.9
sigma_I = 17.6
rho = -0.11

t = 0.2
i = 0.8

#%%
"""""""""""""""""""""""""""""""""""""""
What is the mean of the return on your
portfolio?
"""""""""""""""""""""""""""""""""""""""
mu_R = t*mu_T + i*mu_I
print(mu_R)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the standard deviation of the 
return on your portfolio?
"""""""""""""""""""""""""""""""""""""""
sigma2_R = (t*sigma_T)**2 + (i*sigma_I)**2 + 2*t*i*rho*sigma_T*sigma_I
sigma_R = np.sqrt(sigma2_R)
sigma_R = round(sigma_R, 2)
print(sigma_R)

#%% Lecture Quiz Problem

# Question 4
payout = np.array([68,     -2])
prob = np.array([1/38, 37/38])

mu_X = np.sum(payout * prob)
print(mu_X)

# Question 5
mu_X = 10
mu_Y = 5
sigma_X = 2
sigma_Y = 1
rho = 0

X = 1
Y = 3

variance = (X*sigma_X)**2 + (Y*sigma_Y)**2 + 2*X*Y*rho*sigma_X*sigma_Y
sigma_1 = np.sqrt(variance)
sigma_1 = round(sigma_1, 2)
print(sigma_1)


