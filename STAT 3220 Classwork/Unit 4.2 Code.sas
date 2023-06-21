
*========================================================;
*========================================================;
*     Bird Keeping        ;
*========================================================;
*========================================================;
  
*Some Exploratory Data Analysis;
  
 
proc freq data=ourdata.birdkeeping;
 run;
 
  proc freq data=ourdata.birdkeeping;
 table lungcancer bird;
 run;
 
 
proc freq data=ourdata.birdkeeping;
 table lungcancer*bird /norow nopercent plots=all ;
 run;
 

proc sgplot data=ourdata.birdkeeping;
vbox smoked/category=lungcancer;
run;

*To perform the drop in deviance test, we will not use the 
test statement in SAS, like we did with MLR;

*Complete model;
proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Gender Status Age Smoked Cigarettes Bird;
run;

*Reduced Model;
proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Gender Status Age Smoked Cigarettes;
run;

data calc;
dropstat= 32.9367-21.2668; *calculates the test statistic;
df=6-5; *calculates the DF;
dropcrit= quantile('chisquare',.95,df); 
*computes the rejection region;
droppvalue= sdf('chisquare',dropstat,df); 
*calculates the p-value of the test statistic;
*print the above quantities;
proc print data=calc;
run;

proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Bird;
run;

*Goodness of fit tests and diagnostics;
 proc logistic data=ourdata.birdkeeping plots(only label)=(influence leverage dpc);
 model lungcancer (event='1')=Gender Status Age Smoked Cigarettes Bird/lackfit aggregate scale=none;
run;


/* Classwork */
*Complete model;
proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Gender Status Age Smoked Cigarettes Bird;
run;

*Reduced Model;
proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Gender Status Age Smoked Cigarettes;
run;

*Just Bird;
proc logistic data=ourdata.birdkeeping;
model  LungCancer (event='1')= Bird;
run;





















