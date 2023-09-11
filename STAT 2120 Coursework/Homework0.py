#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:36:38 2022

@author: CarsonCrenshaw
"""

import numpy as np
import pandas as pd
import scipy.stats as stats

mydata = {'Rainfall':[40, 36, 70,
                      74, 20, 55, 32, 37, 84, 29,
                      56, 42, 39, 46],
        
'AQI':[50, 230, 15, 123, 75, 137, 26, 74, 35, 300, 164, 64, 47, 124],

'CO2 (Mt)':[37, 5, 15, 23, 4, 43, 26, 35, 41, 7, 9, 12, 17, 32],

'Factories':[2, 0, 5, 3, 6, 1, 2, 1, 3, 4, 0, 2, 1, 3],

'HealthScore':[69, 54, 15, 32, 57, 26, 21, 45, 17, 24, 63, 34, 47, 12]}

df = pd.DataFrame(mydata)

# Calculate MEAN of CO2 Column
np.mean(mydata['CO2 (Mt)'])

# Calculate STANDARD DEVIATION of Factories column
np.std(mydata['Factories'], ddof = 1)

df['Factories'].describe()

np.std(mydata.iloc[:,3])

# Displaying specific rows for AQI and Health Score columns (by number)
rows = [4,6,7,8,11] 
cols = [1, 4]
df.iloc[rows, cols]

# Displaying specific rows for AQI and Health Score columns (by name)
rows2 = [4,6,7,8,11] 
cols2 = ['AQI', 'Health Score']
df.loc[rows2, cols2]

df.loc[[4,6,7,8,11], ['AQI', 'Health Score']]

# Describing the HealthScore Column
df['Health Score'].describe()

# Displaying Health Score data
df[df['HealthScore'] < 60]

df[df.HealthScore<60]
