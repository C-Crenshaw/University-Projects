
*========================================================;
*========================================================;
*             			Gas Turbine            			 ;
*========================================================;
*========================================================;


*========================================================;

*QUESTION: Do any of the variables seem to have a relationship with 
heat rate?;


proc sgscatter data=ourdata.gasturbine;
	plot heatrate*( AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM)/;
run;

proc sgplot data=ourdata.gasturbine;
vline engine/response=heatrate datalabel stat=mean;
run;

proc sgplot data=ourdata.gasturbine;
vline shafts/response=heatrate datalabel stat=mean;
run;
*note there are only two observations where shafts=3;

proc freq data=ourdata.gasturbine;
table shafts;
run;

	
*========================================================;

*QUESTION: Is there evidence that any of the independent 
variables have a relationship with each other?;



proc corr data=ourdata.gasturbine nosimple plots=matrix rank ; 
*we can add the plots=matrix to produce the scatterplot matrix
and the rank option to rank the correlations for each variable;
var AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM ; 
*we only want to look at how explanatory variables are related;
run;

*========================================================;

*QUESTION: Is there any evidence of multicollinearity?;

proc reg data=ourdata.gasturbine plots=none;
model heatrate = AIRFLOW CPRATIO EXH_TEMP INLET_TEMP power RPM  / vif; 
run;

*add the VIF option to the model statement to get the VIF for 
each explanatory variable;

*========================================================;

*QUESTION: Which model results from using stepwise selection?;

proc reg data=ourdata.gasturbine plots=none;
model heatrate = AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM  / 
selection=stepwise SLentry=0.05 SLstay=0.10 details; 
*The defaults for SLStay (SLS) and SLEntry (SLE) 0.15 for STEPWISE.;
run;

*add the selection option to the model statement;


*========================================================;

*QUESTION: Which model results from using forward selection?;

proc reg data=ourdata.gasturbine plots=none;
model heatrate = AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM  / 
selection=forward SLentry=0.05 details;
*The defaults of SLEntry (SLE) are 0.50 for FORWARD.;
run;


*========================================================;


*QUESTION: Which model results from using backward elimination?;

proc reg data=ourdata.gasturbine plots=none;
model heatrate = AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM  / 
selection=backward SLstay=0.05 details=all;
*The default for SLstay is 0.10 for BACKWARDS Selection;
run;

proc reg data=ourdata.gasturbine plots=none;
model heatrate =   EXH_TEMP INLET_TEMP  RPM /vif  ;
run;


proc reg data=ourdata.gasturbine plots=none;
model heatrate = AIRFLOW CPRATIO EXH_TEMP INLET_TEMP POWER RPM  / 
selection=stepwise SLentry=0.15 SLstay=0.15 details; 
*The defaults for SLStay (SLS) and SLEntry (SLE) 0.15 for STEPWISE.;
run;

*========================================================;
*What should we do next?;

proc reg data=ourdata.gasturbine plots=none;
model heatrate =   EXH_TEMP INLET_TEMP  RPM  / VIF; 
run;

*Since this model seems adequate, we can consider adding 
higher order terms, qualitative varibles, and interactions.;


/* NCAA Classwork Problem */

*QUESTION 2: Are any of the pairwise relationships between explanatory variables strong?;
proc sgscatter data=ourdata.ncaa19;
	matrix FG _3P FT ORB TRB AST STL BLK TOV PF; 
run;

proc corr data=ourdata.ncaa19 nosimple; 
var FG _3P FT ORB TRB AST STL BLK TOV PF; 
run;

*QUESTION 3: Is there any evidence of multicollinearity?;

proc reg data=ourdata.ncaa19 plots=none;
model SRS = FG _3P FT ORB TRB AST STL BLK TOV PF  / vif; 
run;

*QUESTION 4: Which model results from using stepwise selection?;

proc reg data=ourdata.ncaa19 plots=none;
model SRS = FG _3P FT ORB TRB AST STL BLK TOV PF  / 
selection=stepwise details; 
run;


proc reg data=ourdata.ncaa19 plots=none;
model SRS =  BLK TOV TRB AST FT ORB STL  / VIF; 
run;














