"""""""""""""""""""""""""""""""""""""""

Unit 6.1 examples

"""""""""""""""""""""""""""""""""""""""
# Import needed packages
import numpy as np
import pandas as pd
import scipy.stats as stats


# Population parameters
mu = 405.17
sigma = 210.59

#%%
"""""""""""""""""""""""""""""""""""""""
Sampling distribution parameters
"""""""""""""""""""""""""""""""""""""""
sigma_xbar25 = sigma/np.sqrt(25)
sigma_xbar50 = sigma/np.sqrt(50)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that the 
sample mean of a sample of 25 is less 
than $350?
"""""""""""""""""""""""""""""""""""""""
xbar = 350
z = (xbar - mu)/(sigma/np.sqrt(25))

P1 = stats.norm.cdf(z)
P1 = round(P1, 4)
print(P1)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that the 
sample mean of a sample of 50 is less 
than $350?
"""""""""""""""""""""""""""""""""""""""
xbar = 350
z = (xbar - mu)/(sigma/np.sqrt(50))

P2 = stats.norm.cdf(z)
P2 = round(P2, 4)
print(P2)




#%%
"""""""""""""""""""""""""""""""""""""""

Unit 6.1 graphics

"""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

text = pd.read_csv(r"C:\Users\rr3pp\Box\stat2120\Rich\Course materials\Data\textbook.csv")


#%%
"""""""""""""""""""""""""""""""""""""""
Create population histogram
"""""""""""""""""""""""""""""""""""""""
sns.distplot(text.Amount, bins=8, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of amount spent on textbooks")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")


#%%
"""""""""""""""""""""""""""""""""""""""
Create sampling distribution histogram
"""""""""""""""""""""""""""""""""""""""
# Define sample size
my_n = 25 

# Create list to store sample means
means25_list = []

# Draw a sample, calculate and store the sample mean of that sample
# Repeat this process 10,000 times
for i in range(0, 10000):
    samp = text.sample(n=my_n)
    samp_mean = np.mean(samp.Amount)
    means25_list.append(samp_mean)
    
# Display the 10,000 sample means in a histogram
sns.distplot(means25_list, bins=10, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of sample means with n=25")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")
plt.xlim(250,600)


#%%
# Define sample size
my_n = 50 

# Create list to store sample means
means50_list = []

# Draw a sample, calculate and store the sample mean of that sample
# Repeat this process 10,000 times
for i in range(0, 10000):
    samp = text.sample(n=my_n)
    samp_mean = np.mean(samp.Amount)
    means50_list.append(samp_mean)

# Display the 10,000 sample means in a histogram
sns.distplot(means50_list, bins=10, kde=False, color="white", hist_kws=dict(edgecolor="black"))
plt.title("Histogram of sample means with n=50")
plt.ylabel("Frequency")
plt.xlabel("Amount in dollars")
plt.xlim(250,600)