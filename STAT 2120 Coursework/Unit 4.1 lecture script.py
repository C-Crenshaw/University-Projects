"""""""""""""""""""""""""""""""""""""""

Unit 4.1 examples

"""""""""""""""""""""""""""""""""""""""
# Define probabilities
P_R = 0.67
P_N = 0.33


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that you meet 
exactly two VA residents?
"""""""""""""""""""""""""""""""""""""""
P1 = P_R*P_R*P_N + P_R*P_N*P_R + P_N*P_R*P_R
P1 = round(P1,4)
print(P1)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probabiltiy that you meet 
at least two VA residents?
"""""""""""""""""""""""""""""""""""""""
P2 = P_R*P_R*P_N + P_R*P_N*P_R + P_N*P_R*P_R + P_R*P_R*P_R
P2 = round(P2,4)
print(P2)


#%%
"""""""""""""""""""""""""""""""""""""""
What is the probability that the first 
non-resident you meet is the third person you meet?
"""""""""""""""""""""""""""""""""""""""
P3 = P_R*P_R*P_N
P3 = round(P3,4)
print(P3)
