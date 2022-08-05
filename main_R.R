
# installing the packages
install.packages("rstan", repos = c("https://mc-stan.org/r-packages/", getOption("repos")))
install.packages('rstanarm')
install.packages('bayesplot')
install.packages('dplyr')

# calling the libraries
library('rstan')
library('rstanarm')
library('bayesplot')
library(dplyr)

# setting the working directory
setwd('D://Projects/Bayesian-Marketing-Mix-Modeling')

# reading the csv files
data <- read.csv('advertising_data.csv')

# lets build the simple linear regression model first
lmodel <- lm(sales~TV+radio+newspaper, data=data)
summary(lmodel)

# from the summary we observe that the coefficent of newspaper is negative which is practically impossible

# to model this predictors assuming these constraints we can use Bayesian methods for prediction

# setting the prior for the predictors
my_prior <- normal(location = c(0.1, 0.2, 0.1), scale = c(0.001, 0.01, 0.001), autoscale = FALSE)

#fitting the model
fit_2 <- stan_glm(sales~TV+radio+newspaper, data=data, prior=my_prior)

# analysing the results
summary(fit_1)







  




