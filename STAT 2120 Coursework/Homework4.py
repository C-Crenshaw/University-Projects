#%%

Win = 0.52
Lose = 0.48

All_Wins = Win*Win*Win*Win
All_Wins = round(All_Wins,4)
print(All_Wins)

G2 = Lose*Lose
G2 = round(G2,4)
print(G2)

G3 = Win*Lose*Lose*Lose + Win*Lose*Lose*Lose + Win*Lose*Lose*Lose + Win*Lose*Lose*Lose
G3 = round(G3,4)
print(G3)

#%%
X = np.array([1, 2, 4])
P = np.array([1/3, 1/3, 1/3])

# Mean
mu_X = np.sum(X * P)
print(mu_X)

#Standard D
sigma2_X = np.sum((X-mu_X)**2 * P)
sigma_X = np.sqrt(sigma2_X)
sigma_X = round(sigma_X, 4)
print(sigma_X)

#%%
X2= np.array([1.5, 2.5, 3, 1, 2, 4])
P2 = np.array([2/9, 2/9, 2/9, 1/9, 1/9, 1/9])

# Mean
mu_X2 = np.sum(X2 * P2)
print(mu_X2)

#Standard D
sigma2_X2 = np.sum((X2-mu_X2)**2 * P2)
sigma_X2 = np.sqrt(sigma2_X2)
sigma_X2 = round(sigma_X2, 4)
print(sigma_X2)
