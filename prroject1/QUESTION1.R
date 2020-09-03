ds <- read.csv(file.choose(),header = T)
View(ds)

dss<-ds[(ds$PLAYERS_COUNT> 50),]

plot(dss$TIME,dss$PLAYERS_COUNT,xlim=c(0,120),ylim=c(40,160),xlab='TIME',ylab='PLAYERS COUNT',main='SCATTER PLOT(Blue:2/9/20,Green:3/9/20,Black:4/9/20)',type='l')

points(dss$TIME[dss$DATE=='02-09-20'],dss$PLAYERS_COUNT[dss$DATE=='02-09-20'],col='blue', pch=15)
points(dss$TIME[dss$DATE=='03-09-20'],dss$PLAYERS_COUNT[dss$DATE=='03-09-20'],col='green', pch=16)
points(dss$TIME[dss$DATE=='04-09-20'],dss$PLAYERS_COUNT[dss$DATE=='04-09-20'],col='black', pch=17)

