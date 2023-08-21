# Correlation tests are a method for testing linear dependence between 
# two variables 
# As with the other tests we have learned, there are parametric and 
# non-parametric options

data("ToothGrowth")
head(ToothGrowth)
# Let's just look at this correlation first
cor(ToothGrowth$len, ToothGrowth$dose)

# Clearly there's correlation, but it can be good to run a rigorous test to see 
# how significant this correlation is. The first option is the Pearson correlation 
# which is based on a parametric calculation for correlation, so like t- and 
# z-tests, the Pearson test is going to assume that both of your variables have 
# a normal distribution. We run this using the `cor.test` function. 

# Correlation: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

cor.test(ToothGrowth$len, ToothGrowth$dose, method = "pearson")


# But are our variables normally distributed? If not, then this method does not 
# make sense. 
library(ggplot2)
ggplot(ToothGrowth, aes(x = len)) + 
  geom_histogram(aes(y = ..density..), binwidth = 3)
ggplot(ToothGrowth, aes(x = dose)) + 
  geom_histogram(aes(y = ..density..))

# We do not have normality -- especially with dose, which is not continuous. 
# Our other options are Kendall Tau Correlation and Spearman Rho Correlation, 
# which are nonparametric alternatives. These tests differ in how they go about 
# using the ranks of the values to calculate correlation.
# Tau: https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
# Rho: https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient

cor.test(ToothGrowth$len, ToothGrowth$dose, method = "kendall")
cor.test(ToothGrowth$len, ToothGrowth$dose, method = "spearman")

# If you choose to do a correlation test for the final, be sure to review 
# documentation for these forms of correlation and make sure you check all the 
# assumptions -- running them is easy, but making sure you're using the right 
# test is a little more complicated! 
