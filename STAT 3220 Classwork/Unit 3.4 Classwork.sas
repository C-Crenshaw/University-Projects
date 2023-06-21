 OURDATA.WINE2 quality clarity aroma body flavor oakiness OURDATA.WINE2 quality clarity aroma body flavor oakiness *========================================================;
*========================================================;
*					MISS WORK 	(EXERCISE 8.28)			 ;
*========================================================;
*========================================================;
 
 *A Large manufacturing firm wants to determine whether a 
 relationship exists between y, the number of work-hours an
 employee misses per year and x, the employee's annual wages.
 We have a sample of 15 employees.;

proc sgplot data=ourdata.misswork;
scatter x=wages y=hours/ datalabel;
run;

/* *FIT THE MODEL AND CHECK ASSUMPTIONS; */
proc reg data=ourdata.misswork plots(only label)=(residualbypredicted 
residualplot qqplot residualhistogram);
  *We can add "label" in the plots option to identify extreme observations;
 model hours=wages/dwprob; 
 run;
 
 
/*  *There appears to be a violation, but this may be confounded by  */
/*  an extreme observation, let's explore the influential statistics; */
/*   */


 proc reg data=ourdata.misswork plots(only label)=(cooksd 
 rstudentbypredicted rstudentbyleverage); 
*note we are looking at plots of each statistic and include a label
statement to identify which observations are influential or outliers;
model hours=wages / r influence;
*we add the "r" and "influence" options to the model statement to 
output the desired statistics;
run;

*Observation 13 is rxtremely influential with respect to all of our 
influence statistics. We need to investigate this observation further;

/* *We learned that employee #13 had been fired, but his name was not  */
/* removed from the database. In view of this, what is your recommendation */
/* of this outlier?; */

*We should remove this observation from the data table because it
is not representative of our population.;
proc sgplot data=ourdata.misswork;
where hours<500;
scatter x=wages y=hours/ datalabel;
run;


 proc reg data=ourdata.misswork plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model hours=wages / r influence;
reweight obs. = 13;
run;
*We add the REWEIGHT statement. We will use this statement simialr to an If/then
statement and any observations that meet the restriction 
will not be included in our model fitting.;

* You can use the reweight restrict based on the values of 
influential statistics as well.;
 proc reg data=ourdata.misswork plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage); 
model hours=wages / r influence;
reweight cookd. > 0.266;
run;

/* We can also store the influential statistics in our data table. And 
use the new table created to do a similar thing */

 proc reg data=ourdata.misswork plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage); 
model hours=wages / r influence;
output out=mydata.missworkinfl cookd=CooksD residual=Res h=leverage;
run;
*In the output statement, we first define OUT=TABLENAME. This creates a 
new datatable that will have the originial data table and add columns that
you request. For this particular example, we will request the
values of cooks distance, residuals and leverage for each observation. 
You can also store predicted values, interval estimates, and more. 
See the output page for more details;

*Then we will refit the model with the new data;
 proc reg data=mydata.missworkINFL plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage); 
WHERE COOKSD<0.266 and leverage<0.266;
model hours=wages / r influence;
/* output out=mydata.missworkinfl cookd=CooksD residual=Res h=leverage; */
run;

/* To permanenlty delete observations from a  */
/* data table we can use if _ then delete */


data mydata.missworkremove;
set mydata.missworkinfl;
if CooksD > 0.266 then delete;
run;

*The second method is better if you want to remove many observations at one time;
*The first method is better if you have just one observation that you
want to remove and compare the fit model.;

*Refit the model with a higher order term;
data mydata.misswork2;
set ourdata.misswork;
wages2=wages**2;
run;
proc reg data=mydata.misswork2 plots(label);
second_order: model hours= wages wages2;
reweight obs.=13;
first_order: model hours=wages;
reweight obs.=13;
run;



/* In-Class Example */
proc sgscatter data=ourdata.homesalesnew;
	plot price*(size quality qualitysquare dummyb dummyc);
run;

proc reg data=ourdata.homesalesnew plots(only label)=(residualbypredicted 
residualplot qqplot residualhistogram);
  *We can add "label" in the plots option to identify extreme observations;
 model price=size quality qualitysquare dummyb dummyc/dwprob; 
 run;
 
proc reg data=ourdata.homesalesnew plots(only label)=(cooksd 
 rstudentbypredicted rstudentbyleverage); 
*note we are looking at plots of each statistic and include a label
statement to identify which observations are influential or outliers;
model price=size quality qualitysquare dummyb dummyc / r influence;
*we add the "r" and "influence" options to the model statement to 
output the desired statistics;
run;


