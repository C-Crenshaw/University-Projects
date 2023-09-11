"""""""""""""""""""""""""""""""""""""""

Unit 4.4 examples

"""""""""""""""""""""""""""""""""""""""
# Import packages
import numpy as np

# Fill in the amounts associated with spaces A' through I'
X = np.array([ 100, 500, 1000, 0, 10000, 0, 1000, 500, 100])

# Fill in the probabilities that the chip falls into spaces A' through I' when starting at each location
P_A = np.array([ 0.226, 0.387, 0.242, 0.107, 0.032, 0.006, 0, 0, 0])
P_B = np.array([ 0.193, 0.347, 0.247, 0.137, 0.057, 0.016, 0.003, 0, 0])
P_C = np.array([ 0.121, 0.247, 0.241, 0.196, 0.121, 0.054, 0.017, 0.003, 0])
P_D = np.array([ 0.054, 0.137, 0.196, 0.226, 0.193, 0.121, 0.054, 0.016, 0.003])
P_E = np.array([ 0.016, 0.057, 0.121, 0.193, 0.226, 0.193, 0.121, 0.057, 0.016])
P_F = np.array([ 0.003, 0.016, 0.054, 0.121, 0.193, 0.226, 0.196, 0.137, 0.054])
P_G = np.array([ 0, 0.003, 0.017, 0.054, 0.121, 0.196, 0.241, 0.247, 0.121])
P_H = np.array([ 0, 0, 0.003, 0.016, 0.057, 0.137, 0.247, 0.347, 0.193])
P_I = np.array([ 0, 0, 0, 0.006, 0.032, 0.107, 0.242, 0.387, 0.226])


#%%
# Calculate the mean starting at each location
mu_A = np.sum(P_A * X)
print(mu_A)
mu_B = np.sum(P_B * X)
print(mu_B)
mu_C = np.sum(P_C * X)
print(mu_C)
mu_D = round(np.sum(P_D * X), 2)
print(mu_D)
mu_E = np.sum(P_E * X)
print(mu_E)
mu_F = round(np.sum(P_F * X), 2)
print(mu_F)
mu_G = np.sum(P_G * X)
print(mu_G)
mu_H = np.sum(P_H * X)
print(mu_H)
mu_I = np.sum(P_I * X)
print(mu_I)

# Print each mean with this statement modified appropriately
# Round to two decimal places where needed
print("Expected winnings starting at location A is $" + str(mu_A))
print("Expected winnings starting at location B is $" + str(mu_B))
print("Expected winnings starting at location C is $" + str(mu_C))
print("Expected winnings starting at location D is $" + str(mu_D))
print("Expected winnings starting at location E is $" + str(mu_E))
print("Expected winnings starting at location F is $" + str(mu_F))
print("Expected winnings starting at location G is $" + str(mu_G))
print("Expected winnings starting at location H is $" + str(mu_H))
print("Expected winnings starting at location I is $" + str(mu_I))

#%%
# Calculate the standard deviation of winnings starting at each location
sigma_A = np.sqrt(np.sum((X-mu_A)**2 * P_A))
print(sigma_A)
sigma_B = np.sqrt(np.sum((X-mu_B)**2 * P_B))
print(sigma_B)
sigma_C = np.sqrt(np.sum((X-mu_C)**2 * P_C))
print(sigma_C)
sigma_D = np.sqrt(np.sum((X-mu_D)**2 * P_D))
print(sigma_D)
sigma_E = np.sqrt(np.sum((X-mu_E)**2 * P_E))
print(sigma_E)
sigma_F = np.sqrt(np.sum((X-mu_F)**2 * P_F))
print(sigma_F)
sigma_G = np.sqrt(np.sum((X-mu_G)**2 * P_G))
print(sigma_G)
sigma_H = np.sqrt(np.sum((X-mu_H)**2 * P_H))
print(sigma_H)
sigma_I = np.sqrt(np.sum((X-mu_I)**2 * P_I))
print(sigma_I)

# Print each standard deviation with this statement modified appropriately
# Round to two decimal places where needed
print("Standard deviation of winnings starting at location A is $" + str(sigma_A))
print("Standard deviation of winnings starting at location B is $" + str(sigma_B))
print("Standard deviation of winnings starting at location C is $" + str(sigma_C))
print("Standard deviation of winnings starting at location D is $" + str(sigma_D))
print("Standard deviation of winnings starting at location E is $" + str(sigma_E))
print("Standard deviation of winnings starting at location F is $" + str(sigma_F))
print("Standard deviation of winnings starting at location G is $" + str(sigma_G))
print("Standard deviation of winnings starting at location H is $" + str(sigma_H))
print("Standard deviation of winnings starting at location I is $" + str(sigma_I))

#%% Question 5
mu_A = 778.1
mu_E = 2562.2
sigma_A = 1713.35
sigma_E = 4038.06
rho = 0

variance = (sigma_A)**2 + (sigma_E)**2 + 2*A*E*rho*sigma_A*sigma_E
print(variance)
sigma_1 = np.sqrt(variance)
sigma_1 = round(sigma_1, 2)
print(sigma_1)
