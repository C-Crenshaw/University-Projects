"""""""""""""""""""""""""""""""""""

Unit 2.1 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/Crocs.csv"
croc_data = pd.read_csv(filename)


#%%
# Create scatterplot
sns.scatterplot(x='HeadLength', y='BodyLength', data=croc_data)
plt.title("Scatterplot of crocodile information", fontsize = 28)
plt.ylabel("Body Length", fontsize = 14)
plt.xlabel("Head Length", fontsize = 14)

#%%
# Determine correlation
# Calculate correlation (displayed with other information by default)
# Will illustrate correlation combinations between all possible variables (outputs a 2x2 table)
corr = croc_data.corr()

# Subset and round the correlation coefficient (printing correlation value)
r = corr.iloc[0,1]
r = round(r,4)
print("The correlation between these variables is " + str(r) + ".")

#%%
# Read in the data
filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/OKcupid.xlsx"
dating_data = pd.read_excel(filename)

#%%
sns.scatterplot(x='age', y='attractive', hue = 'gender', data=dating_data)
plt.ylim(0,55)
plt.xlim(15,55)
plt.ylabel('Most attractive age to date')
plt.xlabel('Age')

