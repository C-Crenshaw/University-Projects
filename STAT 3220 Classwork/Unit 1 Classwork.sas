/*  */
/*  */
/* Exploratory Data Analysis (EDA) */
/*  */
/*  */

/* Histogram of response variable; */
proc sgplot data=ourdata.nfl2016;
title "Histogram of Wins";
histogram w;
xaxis label="Wins";
run;
title;

/* *Scatter Plots for quantitative variables; */

*this is a comment;

*We could make them one at a time, for example a 
scatter plot for Field Goal Percentage;
proc sgplot data=ourdata.nfl2016;
 title "NFL 2016 Wins vs FGP Scatter Plot"; 
 *a title statement is optional, but easy to add;
scatter x=FGP y=w;
reg x=FGP y=w;
*The reg statement is optional;
run;
title;
*we add the null title statment to clear titles;

*Or, when we have many plots to make at once, we can use
a differnt procedure;
proc sgscatter data= OURDATA.NFL2016;
 title "NFL 2016 Wins vs X Scatter Plots"; 
plot  W*( FGP OffPY OffRY OppPY OppRY PA Penalty TurnoverDiff  );
* plot Y*(x1 x2 x3...);
run;
title;

*========================================================;

*Correlation of quantitaive variables with the response;
proc corr data=ourDATA.NFL2016 pearson nosimple noprob plots=none;
	var OffPY OffRY PA FGP Penalty TurnoverDiff OppPY OppRY;
	with W;
run;

*========================================================;

/*  */
/*  */
/* Fitting & Assessing the Model */
/*  */
/*  */

* We see TurnoverDiff and PA have the strongest linear relationships
Potentially, OppRY has a curvilinear relationship;

*Create the higher order term for OppRY;

data mydata.nfl2016v2; *create a new data table, stored to your files;
set ourdata.nfl2016; *use the original data table as base;
OppRYsq=OppRY**2; *Newvar=function of old var;
run;

*========================================================;
*Fit the model;
proc reg data=mydata.nfl2016v2 plots=none; *use the data name you want to analyze;
model W= TurnoverDiff PA OppRY OppRysq; *model Y= X1 X2 X3...;
run;



*Calculating the critical value for Global F test;
data cutoff;
fcritical=quantile('F',.95,4,27); 
*quantile('f', 1-alpha, numerator df, denominator df);
proc print data=cutoff; 
*this will output the data table we created with the critical value;
run;


*Calculating the critical value for Individual T test;
data cutoff;
tcritical=quantile("t",.975,27); 
*quantile("t",1-(alpha/2),n-k-1);
proc print data=cutoff;
run;

*========================================================;


/*  */
/*  */
/* Remove Higher order term and refit model */
/*  */
/*  */

proc reg data=ourdata.nfl2016 plots=none; *use the data name you want to analyze;
model W= TurnoverDiff PA OppRY;
run;

*========================================================;

/*  */
/*  */
*Confidence Intervals for betas;
/*  */
/*  */
proc reg data=ourdata.nfl2016 plots=none;
model W= TurnoverDiff PA OppRY/clb ;
run;

*We can change the confidence level of the interval;
proc reg data=ourdata.nfl2016 plots=none;
model W= TurnoverDiff PA OppRY/clb alpha=0.01;
run;

*========================================================;
/*  */
/*  */
*Prediction;
/*  */
/*  */

*Because this observation is already in our sample, we can just 
add the options for cli and p to get predictions intervals ;
proc reg data=ourdata.nfl2016 plots=none;
model W= TurnoverDiff PA OppRY / cli;
run;

*NOTE: If we want to find a confidence interval for E(y) we will
use /clm. Similar to intervals for betas, we can specify any level
of significance;

*However, Let's say we wanted to predict a new observation;

*First, create a new data table with the new values
You only need to include the variables in your model;

data pred;
input TurnoverDiff PA OppRY;
cards;
6 331 1652 
;
run;

*Then we add it to the original tabel;
data mydata.nfl2016v3; *new name;
set ourdata.nfl2016 pred; *orignal and prediciton;
run;

proc reg data=mydata.nfl2016v3 plots=none;
model w= TurnoverDiff PA OppRy/cli;
run;


/*  */
/*  */
/* Snow Geese Feeding Trial Example */
/*  */
/*  */

*Histogram of response variable;
*View the response variable to confirm that it is continuous, and approximately unimodal and symmetric;
proc sgplot data=ourdata.snowgeese;
title "Histogram of Geese Weight Change";
histogram WtChange;
xaxis label="Weight Change";
run;
title;

*Exploratory data analysis of multiple variables;
proc sgscatter data= OURDATA.SNOWGEESE;
 title "Geese Weight Change vs X Scatter Plots"; 
plot  WtChange*(  ADFiber DigEff )/columns=1;
* plot Y*(x1 x2 x3...);
run;
title;

*Correlation of quantitaive variables with the response;
proc corr data=OURDATA.SNOWGEESE pearson nosimple noprob plots=none;
	var DigEff ADFiber;
	with WtChange;
run;

*Fitting & Assessing the Model;
* We see DigEff ADFiber have strong linear relationships;
proc reg data=ourdata.snowgeese plots=none; *use the data name you want to analyze;
model WtChange= DigEff ADFiber; *model Y= X1 X2 X3...;
run;

* Critical Values for F-test for model accuracy using α = .01;
data cutoff;
fcritical=quantile('F',.99,2,39); 
*quantile('f', 1-alpha, numerator df, denominator df);
proc print data=cutoff; 
*this will output the data table we created with the critical value;
run;

*Calculating the critical value for Individual T test;
data cutoff;
tcritical=quantile("t",.99,39); 
*quantile("t",1-(alpha/2),n-k-1);
proc print data=cutoff;
run;

*Refit the Model;
proc reg data=ourdata.snowgeese plots=none; *use the data name you want to analyze;
model WtChange= ADFiber;
run;

*Confidence Interval;
proc reg data=ourdata.snowgeese plots=none;
model WtChange= ADFiber/clb alpha=0.02;
run;

*Prediction;
data pred;
input ADFiber;
cards;
15 
;
run;

*Then we add it to the original tabel;
data mydata.snowgeese2; *new name;
set ourdata.snowgeese pred; *orignal and prediciton;
run;

proc reg data=mydata.snowgeese2 plots=none;
model WtChange= ADFiber/cli clm;
run;


/*  */
/*  */
/* Voter Turnout Example */
/*  */
/*  */

*Scatterplots;
proc sgscatter data= OURDATA.POLITICS;
 title "Voters (Y) vs X Scatter Plots"; 
plot  Voted*(  Bachelor_s Christian HealthInsurance MedianIncome NumberPeoplePerFamily Retirement Unemployed  );
* plot Y*(x1 x2 x3...);
run;
title;

*Fitting & Assessing the Model;
* We see Employed Retirement and HealthInsurance have strong linear relationships;
proc reg data=ourdata.politics plots=none; *use the data name you want to analyze;
model Voted= Unemployed NumberPeoplePerFamily HealthInsurance ; *model Y= X1 X2 X3...;
run;

*Critical F Test;
data cutoff;
fcritical=quantile('F',.95,3,46); 
*quantile('f', 1-alpha, numerator df, denominator df);
proc print data=cutoff; 
*this will output the data table we created with the critical value;
run;

*Individual T Test;
data cutoff;
tcritical=quantile("t",.95,46); 
*quantile("t",1-(alpha/2),n-k-1);
proc print data=cutoff;
run;

*Confidence Intervals for betas;
proc reg data=ourdata.politics plots=none;
model Voted= Unemployed NumberPeoplePerFamily HealthInsurance/clb ;
run;

*Prediction;
proc reg data=ourdata.politics plots=none;
model Voted= Unemployed NumberPeoplePerFamily HealthInsurance / cli;
run;

proc reg data=ourdata.politics plots=none;
model Voted= NumberPeoplePerFamily HealthInsurance / cli;
run;



