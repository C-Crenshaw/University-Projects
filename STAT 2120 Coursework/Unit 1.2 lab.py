"""""""""""""""""""""""""""""""""""

Unit 1.2 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import scipy.stats as stats

#%%

"""""""""""""""""""""""""""""""""""""""
Question 1
"""""""""""""""""""""""""""""""""""""""
# Z-scores of interest
z1 = -1
z2 = 1

# Find the proportion between the relevant z-scores
prop = stats.norm.cdf(z2) - stats.norm.cdf(z1)
prop = round(prop,4)
print(prop)

#%%

"""""""""""""""""""""""""""""""""""""""
Question 2
"""""""""""""""""""""""""""""""""""""""
# Z-scores of interest
z1 = -2
z2 = 2

# Find the proportion between the relevant z-scores
prop = stats.norm.cdf(z2) - stats.norm.cdf(z1)
prop = round(prop,4)
print(prop)

#%% Finding the mean and std of Adult golden hamsters

"""""""""""""""""""""""""""""""""""""""
Question 3
"""""""""""""""""""""""""""""""""""""""

# Values of interest (bottom 25 percent)
# Finding z score from area to the left (no subtraction)
prop_top = .25
prop = prop_top

# Find the z-score with this proportion above it.
z = stats.norm.ppf(prop)
print(z)

# Values of interest (top 25 percent)
# Finding z score from area to the right (must subtract)
prop_top2 = .25 
prop2 = 1 - prop_top

# Find the z-score with this proportion above it.
z2 = stats.norm.ppf(prop2)
print(z2)

# Find the MEAN and STD of the dataset

from sympy import symbols, Eq, solve

x, y = symbols('x y')

eq1 = Eq(x - 0.674*y - 4.1)
eq2 = Eq(x + 0.674*y - 4.7)

solve((eq1,eq2), (x, y))

sol_dict = solve((eq1,eq2), (x, y))
print(f'mu = {sol_dict[x]}')
print(f'sigma = {sol_dict[y]}')

# Alternatively, if you find the mean on paper use this calculation to find
# the standard deviation

x2 = 4.7
mu = 4.4
sigma = (x2-mu)/z2
print(sigma)

#%%

"""""""""""""""
Question 4A
"""""""""""""""
# Define the distribution
mu = 30
sigma = 8

# Value of interest
x = 34

# Calculate the z-score
z = (x-mu)/sigma
print(z)

# Find the proportion to the right and round to three decimals.
prop = stats.norm.cdf(z)
prop_above = 1-prop
prop_above = round(prop_above, 3)
print("The proprotion of cardholders greater than " + str(x) + " is " + str(prop_above) + ".")

#%%

"""""""""""""""
Question 4B
"""""""""""""""
mu = 30
sigma = 8

# Values of interest
x1 = 27
x2 = 34

# Calculate the z-scores
z1 = (x1-mu)/sigma
z2 = (x2-mu)/sigma
print(z1)
print(z2)

# Find the proportion between and round to three decimals.
prop = stats.norm.cdf(z2) - stats.norm.cdf(z1)
prop = round(prop, 3)
print("The proprotion of cardholders between " + str(x1) + " and " + str(x2) + " is " + str(prop) + ".")

#%%

"""""""""""""""
Question 4C
"""""""""""""""
mu = 30
sigma = 8

# Values of interest
x1 = 27
x2 = 41

# Calculate the z-scores
z1 = (x1-mu)/sigma
z2 = (x2-mu)/sigma
print(z1)
print(z2)

# Find the proportion to the left for 27 and round to three decimals.
prop = stats.norm.cdf(z1)
prop = round(prop, 3)
print(prop)

# Greater than 41
prop2 = stats.norm.cdf(z2)
prop_above = 1-prop2
print(prop_above)

# Find the proportion together and round to three decimals.
together = prop + prop_above
together = round(together, 3)
print(together)
print("The proprotion of the cardholders between " + str(x1) + " and " + str(x2) + " is " + str(together) + ".")

#%%

"""""""""""""""
Question 4D
"""""""""""""""
# Values of interest
prop_top = .14 
prop = 1 - prop_top

# Find the z-score with this proportion above it.
z = stats.norm.ppf(prop)

# Unstandardize z-score
x = z*sigma + mu
x = round(x, 1)
print("The interest payment that is exceeded by only 14% of the bank’s Visa cardholders is " + str(x) + " dollars.")

















