"""""""""""""""""""""""""""""""""""""""

Question 4

"""""""""""""""""""""""""""""""""""""""

# Define probabilities
P_A = 0.87
P_M = 0.13

#%% 
"""""""""""""""""""""""""""""""""""""""
2 Workouts
"""""""""""""""""""""""""""""""""""""""
#Probability of attending both workouts
P1 = P_A*P_A
P1 = round(P1,4)
print(P1)

#Probability of missing both workouts
P2 = P_M*P_M
P2 = round(P2,4)
print(P2)

#Probability of only attending one workout
P3 = P_A*P_M + P_M*P_A
P3 = round(P3,4)
print(P3)

#%% 
"""""""""""""""""""""""""""""""""""""""
3 Workouts
"""""""""""""""""""""""""""""""""""""""
# Prob of attending all workouts
P11 = P_A*P_A*P_A
P11 = round(P11,4)
print(P11)

# Prob of missing the third workout
P22 = P_A*P_A*P_M
P22 = round(P22,4)
print(P22)

# Prob of missing at least one workout
P33 = P_A*P_A*P_M + P_A*P_M*P_A + P_M*P_A*P_A + P_A*P_M*P_M + P_M*P_A*P_M + P_M*P_M*P_A + P_M*P_M*P_M
P33 = round(P33,4)
print(P33)
