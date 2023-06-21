*========================================================;
*========================================================;
*                HW Help                ;
*========================================================;
*========================================================; 
*QUESTION: Is there evidence of a relationship between 
the homework assistance group and the improvement score;

*We want to look at the mean response of each group,
so we will create a line plot using the "line chart"
task. This is code generated from the "line chart" task
or you can simply use this for future reference.;

proc sgplot data=ourDATA.HWImprove;
	vline ASSIST / response=IMPROVE datalabel stat=mean;
	*vline CATEGORICALVARIABLE / response=RESPONSEVARIABLE datalabel stat=mean;
	*We put stat=mean because we want to see the mean value of y for each
	level of the response;
run;

*We can also examine boxplots of the resposne for each 
level of the qualitative variable to get a better idea of how much 
variability is in the data;

proc sgplot data=ourDATA.HWImprove;
	vbox improve / category=assist ;
	*vbox RESPONSE /category=QUALITATIVE;
run;


*========================================================; 

*QUESTION: Fit the model to the data and give the least 
squares prediction equation. Perform the Global F test;
*FIRST we need to create the dummy variabels in SAS;
*REMINDER: We will define the "no help" as the base level;
/* DummyCH= 1 if Check, 0 otherwise */
/* DummyCO= 1 if Full solution, 0 otherwise */

data mydata.HWImprove1 ; *create a new data set saved to your library called HWImprove1;
	set ourDATA.HWImprove; *set with the original;
	DummyCH=0; *create a varaible called DummyCH where every observation will have a value of 0;
	DummyCO=0; *create a varaible called DummyCO where every observation will have a value of 0;
	if  assist= 'CH' then DummyCH=1; *if the group is CH, then the dummy var will recode to 1;
	if assist='CO' then DummyCO=1; *similarly to above;
run;

*You can print to see that the new data set has the dummy 
variables in the way you want;

proc print data=mydata.HWImprove1;
run;

/* Now run the regular proc reg step to perform the regression 
analysis */

proc reg data=mydata.HWImprove1 plots=none;
model improve=dummych dummyco;
run;

