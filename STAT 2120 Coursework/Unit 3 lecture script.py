"""""""""""""""""""""""""""""""""""""""

Unit 3 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import pandas as pd

# Read in data
stores = pd.read_excel(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/fiveguys_excel.xlsx")


#%%
"""""""""""""""""""""""""""""""""""""""
Simple random sample
"""""""""""""""""""""""""""""""""""""""
# Define the sample size
my_n = 10

# Draw the random sample
samp_stores = stores.sample(n=my_n)
print(samp_stores)


#%%
"""""""""""""""""""""""""""""""""""""""
Stratified sample
"""""""""""""""""""""""""""""""""""""""
# Define the sample size for each stratum (Region)
my_n = 4

# Draw the random sample from each stratum (Region)
strat_stores = stores.groupby('Region').apply(lambda x: x.sample(n=my_n))
print(strat_stores)
