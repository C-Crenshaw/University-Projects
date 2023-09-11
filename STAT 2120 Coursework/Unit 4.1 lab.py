"""""""""""""""""""""""""""""""""""

Unit 4.1 lab activity

"""""""""""""""""""""""""""""""""""
# Install needed packages
import random
import numpy as np
import itertools

# Define the sample space with all possible outcomes of a flip
SS = ['H ','T ']

# Define the number of flips
my_n = 75

# Generate the outcomes
outcomes = random.choices(SS, k=my_n)
print(outcomes)

print(max(sum(1 for _ in l) for n, l in itertools.groupby(outcomes)))

#%%
P_H = 0.60
P_T = 0.40

P1 = P_H*P_T*P_T + P_T*P_H*P_T + P_T*P_T*P_H
P1 = round(P1,4)
print(P1)

P2 = P_H*P_T*P_T + P_T*P_H*P_T + P_T*P_T*P_H + P_H*P_H*P_H + P_H*P_H*P_T + P_H*P_T*P_H + P_T*P_H*P_H
P2 = round(P2, 4)
print(P2)

P3 = P_H*P_T*P_T*P_T + P_T*P_H*P_T*P_T + P_T*P_T*P_H*P_T + P_T*P_T*P_T*P_H
P3 = round(P3, 4)
print(P3)

P4 = P_H*P_T*P_T*P_T + P_T*P_H*P_T*P_T + P_T*P_T*P_H*P_T + P_T*P_T*P_T*P_H + P_H*P_H*P_H*P_H + P_H*P_H*P_T*P_T + P_H*P_T*P_H*P_T + P_T*P_H*P_H*P_T + P_T*P_T*P_H*P_H + P_T*P_H*P_T*P_H + P_H*P_T*P_T*P_H + P_T*P_H*P_H*P_H + P_H*P_T*P_H*P_H + P_H*P_H*P_T*P_H + P_H*P_H*P_H*P_T
print(P4)
