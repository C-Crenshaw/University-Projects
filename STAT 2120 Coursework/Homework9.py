# Import needed packages
import numpy as np
import scipy.stats as stats

#%% Question 1
# Hypothesis Test
#H_0: p = 0.5
#H_a: p >0.5
# alpha = 0.1

p0 = 0.5

#  Sample and known values
n = 1006
phat = .51 

# Test statistic
test_stat = (phat - p0)/np.sqrt(p0*(1-p0)/n)
print(test_stat)
#Step 2: z = 0.63435

# p-value; test is right-tailed
pval = 1 - stats.norm.cdf(test_stat)
print(pval)

n*(1-p0)
n*p0

# Confidence Interval
# Determine z*
z_star = stats.norm.ppf(0.95)
z_star = round(z_star, 3)
print(z_star)

# Determine confidence interval
LL = phat - z_star * np.sqrt(phat*(1-phat)/n)
UL = phat + z_star * np.sqrt(phat*(1-phat)/n)

print(round(LL,3))
print(round(UL,3))

n*phat
n*(1-phat)

moe = z_star * np.sqrt(phat*(1-phat)/n)
print(moe)

#%% Question 2

social = pd.read_csv("/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/social_media.csv")

# Chi-Squared Test
tw_tbl = pd.crosstab(index=social.AgeGroup, columns=social.Hard,
                            margins=True)
print(tw_tbl)

ct = tw_tbl.All[0:2]                            # Isolates column totals
rt = tw_tbl.loc["All"][0:2]                     # Isolates row totals
rtimesc = np.outer(ct,rt)                       # Multiplies the column and row totals appropriately
exp = rtimesc/tw_tbl.loc["All","All"]           # Divides all column and row total products by the sample size
exp = np.round(exp, 2)                          # Rounds the expected counts
exp = pd.DataFrame(exp)                         # Creates a DataFrame
exp.columns = ["no","yes"]     # Names the DataFrame columns
exp.index = ["Over50","Under50"]        # Names the DataFrame rows
print(exp)

# Isolate the observed counts from the two-way table
obs = tw_tbl.iloc[0:2,0:2]
print(obs)

# Determine test statistic components
test_stat_all = (obs - exp)**2 / exp
print(test_stat_all)

# Determine test statistic
test_stat = np.sum(test_stat_all).sum()
test_stat = round(test_stat, 2)
print(test_stat)

# Determine p-value
pval = 1 - stats.chi2.cdf(test_stat, df=4)
pval = round(pval, 4)
print(pval)

# Hypothesis Test; yes/no Hard and Over50
n1 = 800
n2 = 1153
X1 = 409
X2 = 664

phat1 = X1/n1
print(phat1)
phat2 = X2/n2
print(phat2)
phat = (X1 + X2)/(n1 + n2)  

# Test statistic
test_stat = (phat1 - phat2)/np.sqrt(phat*(1-phat)*(1/n1 + 1/n2))
print(test_stat)

# p-value; test is two-tailed
pval = 2 * stats.norm.cdf(-abs(test_stat))
print(pval)

# Confidence Interval
z_star2 = stats.norm.ppf(0.975)
z_star2 = round(z_star2, 3)
print(z_star2)

# Determine confidence interval
LL2 = (phat1 - phat2) - z_star2 * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)
UL2 = (phat1 - phat2) + z_star2 * np.sqrt(phat1*(1-phat1)/n1 + phat2*(1-phat2)/n2)

print(round(LL2,3))
print(round(UL2,3))

#%% Question 3

teststat = ((133-170.88)**2)/170.88 + ((96-92.56)**2)/92.56 + ((139-113.92)**2)/113.92 + ((133-142.4)**2)/142.4 + ((108-92.56)**2)/92.56 + ((103-99.68)**2)/99.68
print(teststat)

pval = 1 - stats.chi2.cdf(17.35, df=7)
pval = round(pval, 4)
print(pval)




