"""""""""""""""""""""""""""""""""""""""

Unit 1.2 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import scipy.stats as stats

#%%
"""""""""""""""""""""""""""""""""""""""
Normal distribution curve proportions
"""""""""""""""""""""""""""""""""""""""
# Define the distribution
mu = 69
sigma = 2.5

""" 1 """
"""""""""""""""""""""""""""""""""""""""
What proportion of men aged 20-29 are
shorter than 66 inches?
"""""""""""""""""""""""""""""""""""""""
# Value of interest
x = 66

# Calculate the z-score
z = (x-mu)/sigma
print(z)

# Find the proportion to the left and round to three decimals.
prop = stats.norm.cdf(z)
prop = round(prop, 3)
print("The proprotion of heights less than " + str(x) + " is " + str(prop) + ".")

# Greater than 66
prop_above = 1-prop
print(prop_above)

#%%
""" 2 """
"""""""""""""""""""""""""""""""""""""""
What proportion of men aged 20-29 are
between 66 and 70 inches tall?
"""""""""""""""""""""""""""""""""""""""
# Values of interest
x1 = 66
x2 = 70

# Calculate the z-scores
z1 = (x1-mu)/sigma
z2 = (x2-mu)/sigma
print(z1)
print(z2)

# Find the proportion between and round to three decimals.
prop = stats.norm.cdf(z2) - stats.norm.cdf(z1)
prop = round(prop, 3)
print("The proprotion of heights between " + str(x1) + " and " + str(x2) + 
      " is " + str(prop) + ".")

#%%
""" 3 """
"""""""""""""""""""""""""""""""""""""""
How tall are the tallest 10% of men
aged 20-20?
"""""""""""""""""""""""""""""""""""""""
# Values of interest
prop_top = .1 
prop = 1 - prop_top

# Find the z-score with this proportion above it.
z = stats.norm.ppf(prop)

# Unstandardize z-score
x = z*sigma + mu
x = round(x, 1)
print("The tallest 10% are at least " + str(x) + " inches tall.")

