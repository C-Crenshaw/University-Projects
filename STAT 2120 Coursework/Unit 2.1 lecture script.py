"""""""""""""""""""""""""""""""""""""""

Unit 2.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd

# Read in data and subset to relevant columns
# NOTE: this csv file has atypical encoding. We don't need to worry too much about detials here,
# But notice that this requires an extra argument (sometimes files need more than just the path)
beer = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/beer.csv", encoding='cp1252')
beer_sub = beer[['PercentAlcohol','CaloriesPer12Oz']]

print(beer_sub)
# Calculate correlation (displayed with other information by default)
# Will illustrate correlation combinations between all possible variables (outputs a 2x2 table)
corr = beer_sub.corr()

# Subset and round the correlation coefficient (printing correlation value)
r = corr.iloc[0,1]
r = round(r,4)
print("The correlation between these variables is " + str(r) + ".")

#%%
"""""""""""""""""""""""""""""""""""""""

Unit 2.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#%%
"""""""""""""""""""""""""""""""""""""""
Create scatterplot
"""""""""""""""""""""""""""""""""""""""
beer = pd.read_csv(r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/beer.csv", encoding='cp1252')

sns.scatterplot(x="PercentAlcohol", y="CaloriesPer12Oz", data=beer)
plt.title("Scatterplot of beer information", fontsize = 28)
plt.ylabel("Calories per 12 ounces", fontsize = 14)
plt.xlabel("Percent alcohol", fontsize = 14)

