*========================================================;
*========================================================;
*					Pre Recorded 3.1							 ;
*========================================================;
*========================================================;

*========================================================;
*========================================================;
*             			Pharmacy            			 ;
*========================================================;
*========================================================;


*========================================================;

*QUESTION: Do any of the variables seem to have a relationship with 
prescription sales?;


proc sgscatter data=ourdata.prescript;
	plot sales*(FloorSp prespct parking income);
run;

proc sgplot data=ourdata.prescript;
vline shopctr/response=sales datalabel stat=mean;
run;

	
*========================================================;

*QUESTION: Is there evidence that any of the independent 
variables have a relationship with each other?;

proc sgscatter data=ourdata.prescript;
	matrix FloorSp prespct parking income; 
	*we only want to look at how explanatory 
	variables are related;
run;


*========================================================;

*QUESTION: Are any of the pairwise relationships between 
explanatory variables strong?;

proc corr data=ourdata.prescript nosimple; 
var FloorSp PresPct Parking Income; 
*we only want to look at how explanatory variables are related;
run;


*========================================================;

*QUESTION: Is there any evidence that the variable income is 
providing redundant information?;

proc reg data=ourdata.prescript plots=none;
model Income = FloorSp PresPct Parking ; 
run;

*We will look at one explanatory variable predicted by the rest.
we are only going to do this in this example, it is not something you
would do in practice;

*========================================================;

*QUESTION: Is there any evidence of multicollinearity due to 
income or other explanatory variables?;

proc reg data=ourdata.prescript plots=none;
model Sales = FloorSp PresPct Parking Income  / vif; 
run;

*add the VIF option to the model statement to get the VIF for 
each explanatory variable;

*========================================================;

*QUESTION: Which model results from using stepwise selection?;

proc reg data=ourdata.prescript plots=none;
model Sales = FloorSp PresPct Parking Income  / 
selection=stepwise SLentry=0.05 SLstay=0.10 details; 
*The defaults for SLStay (SLS) and SLEntry (SLE) 0.15 for STEPWISE.;
run;

*add the selection option to the model statement;


*========================================================;

*QUESTION: Which model results from using forward selection?;

proc reg data=ourdata.prescript plots=none;
model Sales = FloorSp PresPct Parking Income  / 
selection=forward SLentry=0.05 details;
*The defaults of SLEntry (SLE) are 0.50 for FORWARD.;
run;


*========================================================;


*QUESTION: Which model results from using backward elimination?;

proc reg data=ourdata.prescript plots=none;
model Sales = FloorSp PresPct Parking Income  / 
selection=backward SLstay=0.05 details=all;
*The default for SLstay is 0.10 for BACKWARDS Selection;
run;

*========================================================;
*========================================================;
*              Recorded Lecture  3.3           ;
*========================================================;
*========================================================; 


*========================================================;
*========================================================;
*              Mileage Example             ;
*========================================================;
*========================================================; 

*Residual plot for linear model;
proc reg data=ourdata.tires plots(only)=(residualplot  );
 model mileage_y=press_x;
run;

*Create higher order term;
data mydata.tires2;
set ourdata.tires;
Press2=press_x**2;
run;

*Residual Plots with second order model;
proc reg data=mydata.tires2 
plots(only)=(residualbypredicted residualplot qqplot residualhistogram);
 model mileage_y=press_x press2;
run;


*========================================================;
*========================================================;
*              Time Series Example             ;
*========================================================;
*========================================================; 

 proc reg data=ourdata.buypower 
 plots(only) = (ResidualbyPredicted QQPlot ResidualPlot);
model value = t / dwprob; *DWPROB for Durbin Watson;
run;


*========================================================;
*========================================================;
*              Demand Example             ;
*========================================================;
*========================================================; 

*Utility Example;
proc reg data=ourdata.utility 
plots(only)=(residualbypredicted residualplot qqplot 
  residualhistogram); 
  *You can select one or all of the plot options;
 model demand=usage/dwprob; 
 *DWPROB option gives Durbin Watson test;
run;

*Transform RESPONSE variable;
data mydata.utility2;
 set ourdata.utility;
 sqrtdemand=demand**0.5; 
 sqd=sqrt(demand); *SQRT() is the function;
run;

*We use new data and NEW RESPONSE to refit the model;
proc reg data=mydata.utility2 
plots(only)=(residualbypredicted residualplot qqplot 
  residualhistogram);
 model sqrtdemand=usage/dwprob;
 run;
 
*What is a conservative estimate for peak-hour 
 demand when total monthly usage is 679 kWh?;
 
data pred;
input usage;
cards;
679
;
run;
data mydata.utility3;
set mydata.utility2 pred;
run;

proc reg data=mydata.utility3 plots=none;
 model sqrtdemand=usage /  cli clm;
 run;

*Compare to untransformed model;
proc reg data=ourdata.utility plots=none;
 model demand=usage / cli clm;
 run;
 
 
 *========================================================;
*========================================================;
*					Pre Recorded 3.4							 ;
*========================================================;
*========================================================;

*========================================================;
*========================================================;
*					Electric Utility							 ;
*========================================================;
*========================================================;

*Check assumptions with transformed varaible;
proc reg data=mydata.utility2 plots(only)=(residualbypredicted residualplot qqplot 
  residualhistogram);
 model sqrtdemand=usage/dwprob;
 run;
 
 proc reg data=mydata.utility2 plots(only label)=(residualbypredicted residualplot qqplot 
  residualhistogram);
 model sqrtdemand=usage/dwprob;
 run;
 
 *Check for outliers and influential observations;
 
 proc reg data=mydata.utility2 plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage); 
*note we are looking at plots of each statistic and include a label
statement to identify which observations are influential or outliers;
model sqrtdemand=usage / r influence;
*we add the "r" and "influence" options to the model statement to 
output the desired statistics;
run;

proc sgscatter data=mydata.utility2;
plot (sqrtdemand demand)*usage/datalabel=usage;
run;

*Remove Observation 50;
 proc reg data=mydata.utility2 plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model sqrtdemand=usage / r influence;
reweight obs.=50;
* this statement will remove the lsited observations;
*obs. is an automatically created variable that is stored in SAS;
run;

*Remove Observation 26;
 proc reg data=mydata.utility2 plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model sqrtdemand=usage / r influence;
reweight obs.=26;
run;

*Remove both 50 and 26;
 proc reg data=mydata.utility2 plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model sqrtdemand=usage / r influence;
reweight obs.= 26 ;
reweight obs.= 50 ;
run;

 