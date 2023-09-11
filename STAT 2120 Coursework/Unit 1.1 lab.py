"""""""""""""""""""""""""""""""""""

Unit 1.1 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read in the frog jumps data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/frog jumps.xlsx"
frog_data = pd.read_excel(filename)


#%%
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Boxplots can be created for multiple groups and displayed
together in the same graphic by specifying the variable 
containing the group designations in the x input.

The sample mean can be shown by using the showmeans input.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Create side-by-side boxplots
    # Fill in missing values
box = sns.boxplot(x='Paper_Type', y='Distance', data=frog_data, showmeans=True, width=0.5)
plt.setp(box.artists, fill=False, edgecolor="k")
plt.title("Triple jump distance by paper type")


#%%
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
A DataFrame can be subset to rows that contain certain 
values within a given column. A logical expression is used
to assess the values in that column yielding either a True
or False for each row. Rows with a True will be included 
in the subset and rows with a False will be excluded.
Logical operators:
    ==  equal to
    !=  not equal to 
    <   less than
    <=  less than or equal to
    >   greater than
    >=  greater than or equal to
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Subset data to only frogs made with construction paper
constr_data = frog_data[frog_data.Paper_Type == 'Construction']

#%%

print(constr_data)

# Finding the 5 number summary, mean, standard deviation
constr_data.describe()

# Confirming that the median is correctly displayed
np.median(constr_data['Distance']) 

# Confirming that the standard deviation and mean is the same
np.std(constr_data['Distance'])
np.mean(constr_data['Distance']) 

np.max(constr_data)

#%%
# Subset data to only frogs made with copy paper
copy_data = frog_data[frog_data.Paper_Type == 'Copy']

print(copy_data)

# Finding the 5 number summary, mean, standard deviation
copy_data.describe()

# Confirming that the median is correctly displayed
np.median(copy_data['Distance']) 

np.std(copy_data)
