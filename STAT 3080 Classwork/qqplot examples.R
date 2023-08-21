xdatanorm <- data.frame(X = rnorm(100))
ggplot(xdatanorm, aes(x = X)) + geom_histogram()
ggplot(xdatanorm, aes(sample = X)) + stat_qq() + stat_qq_line()

xdatanorm2 <- data.frame(X = rnorm(100))
ggplot(xdatanorm2, aes(sample = X)) + stat_qq() + stat_qq_line()

xdatachisq <- data.frame(X = rchisq(100,2))
ggplot(xdatachisq, aes(x = X)) + geom_histogram()
ggplot(xdatachisq, aes(sample = X)) + stat_qq() + stat_qq_line()

xdatabimod <-data.frame(X = c(rnorm(50), rnorm(50,mean=3,sd=1)))
ggplot(xdatabimod, aes(x = X)) + geom_histogram()
ggplot(xdatabimod, aes(sample = X)) + stat_qq() + stat_qq_line()                        

group <- c(rep("Y",50), rep("N",50))
xdatabimod$group <- group
ggplot(xdatabimod, aes(x = X, fill=group)) + geom_histogram()
ggplot(xdatabimod, aes(sample = X, fill=group)) + stat_qq() + stat_qq_line() 
