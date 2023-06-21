
*========================================================;
*========================================================;
*     Tin Lead       ;
*========================================================;
*========================================================;

*Post Hoc Analysis;
proc anova data=ourdata.tinlead;
class antimony method; *put both main effects;
model strength=antimony method;
means antimony/tukey lines cldiff ;
run;

*Check Assumptions;
*1. Create a histogram. The treatment sizes are too small
so we make a histogram of the entire sample;

proc sgplot data=ourdata.tinlead;
histogram strength;
run;

*2. Check constant variance. Using Bartlett's 
test because the data are approximately normal.;
proc anova data=ourdata.tinlead;
class antimony ; 
model strength=antimony ;
means antimony/hovtest=bartlett;
run;


*========================================================;
*========================================================;
*     Towels       ;
*========================================================;
*========================================================;

*Perform the Two Way ANOVA;
proc anova data=ourdata.towels;
class brand water;
model strength= brand water brand*water;
means brand*water/tukey cldiff lines;
run;

*NOTE: PROC ANOVA does not compute the post hoc
test for interactions;

*So, we use PROC GLM;

proc glm data=OURDATA.TOWELS;
	class Brand Water;
	model Strength= Brand Water Brand*Water;
	lsmeans Brand*Water / adjust=tukey cl;
	*Add the lsmeans statement with the interaction;
run;


*========================================================;

*QUESTION: Do these data violate the assumptions of ANOVA?;

*1. Populations for EACH TREATMENT are normal;

*Histogram of each treatment;

proc sgpanel data=ourdata.towels;
panelby Brand Water/ columns=3;
histogram strength;
density strength /type=normal;
run;

*We can also use this to see the distributon of one
main effect;
proc sgpanel data=ourdata.towels;
panelby Brand ;
histogram strength;
density strength /type=normal;
run;


*2. Population variances of treatments are equal;

*Similarly, if we wanted boxplots for each treatment;
proc sgpanel data=ourdata.towels;
panelby Brand Water/ columns=3;
vbox strength;
run;

*levene's test (non-normal);
proc anova  data=OURDATA.TOWELS;
	class Brand Water;
	model Strength= Brand Water Brand*Water;
	means Brand*Water / hovtest=levene(type=abs);
run;
*We get a warning with interaction model;

*So we can fit main effects instead;
proc anova  data=OURDATA.TOWELS;
	class Brand Water;
	model Strength= brand ;
	means brand / hovtest=levene(type=abs);
run;

proc anova  data=OURDATA.TOWELS;
	class Brand Water;
	model Strength= Water ;
	means Water / hovtest=levene(type=abs);
run;





