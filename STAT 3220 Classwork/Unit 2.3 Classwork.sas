*========================================================;
*========================================================;
*              Recorded Lecture             ;
*========================================================;
*========================================================; 
*========================================================;
*========================================================; 
/* Fuel Example */
*========================================================;
*========================================================; 
*Nested F-test the long way;

proc reg data= mydata.diesel1 plots=none;
complete: model perform= x1 x2 x3 x1x3 x2x3;
test x1x3, x2x3 ;
run;

*========================================================;
*========================================================;
*               CLASS            ;
*========================================================;
*========================================================; 

*========================================================;
*========================================================;
*               Navy Fleet              ;
*========================================================;
*========================================================; 

*========================================================;

proc reg data=mydata.naval3 plots=none;
model percent= cost cost2 basecode costbase cost2base;
test basecode, costbase, cost2base; 
*include the variables that are in the hypothesis separated by commas;
run;


*========================================================;
*========================================================;
*                HOMESALES                 ;
*========================================================;
*========================================================; 

*EDA;
proc sgscatter data=MYDATA.homesalesnew;
	plot price* (quality size)/columns=1;
run;


proc sgplot data=MYDATA.homesalesnew;
	vline school / response=price datalabel stat=mean;
run;


*create all of the terms we need;
data Userdata.homesalesnew1 ; *create a new data set saved to your library called homesales2;
	set MYDATA.homesalesnew; *set with the original table ;
	qualitysquare=quality**2;* a double asterik is the ^ in SAS;
	sizequal=size*quality; *interaction;
	sizequal2=size*qualitysquare; *higher order interaction;
	DummyB=0; *create a varaible called DummyB where every observation will have a value of 0;
	DummyC=0; *create a varaible called DummyC where every observation will have a value of 0;
	if  school = 'B' then DummyB=1; *if the group is B, then the dummy var will recode to 1;
	if school='C' then DummyC=1; *similarly to above;
run;


*1. Fit model with all quant predictors;
proc reg data=Userdata.homesalesnew1 plots=none;
model price = size quality qualitysquare sizequal sizequal2;
run;

*2. Global Test is signifiant, test the sizeXqual interaction;
proc reg data=Userdata.homesalesnew1 plots=none;
model price = size quality qualitysquare sizequal sizequal2;
test sizequal, sizequal2;
run;

*3. remove interactions and refit;
proc reg data=Userdata.homesalesnew1 plots=none;
model price = size quality qualitysquare;
run;

/*  */
/*  */
/* T TEST for Qual^2 is significant. We will move on. */
/*  */
/*  */



*1. Add School District to the model and perform nested F test;
proc reg data=Userdata.homesalesnew1 plots=none;
model price = size quality qualitysquare dummyb dummyc;
test dummyb, dummyc;
run;

/*  */
/*  */
/*  NESTED F TEST for School District is significant. 
We will move on. */
/*  */
/*  */

/*  */
/*  */
/* Pause for some interaction EDA */
/*  */
/*  */

/* Does there appear to be an interaction between school 
district and either quantitaive varaible? */

proc sgplot data=mydata.homesalesnew;
scatter x=size y=price/group=school;
reg x=size y=price/group=school;
run;


proc sgplot data=mydata.homesalesnew;
scatter x=quality y=price/group=school;
reg x=quality y=price/group=school;
run;

/* There appears to be an interaction between School District and Size */
data Userdata.homesalesnew2;
set Userdata.homesalesnew1;
DummyBSize=DummyB*size;
DummyCSize=DummyC*size;
run;

/*  */
/*  */
/*  */
/*  */
/*  */

*1. Add school X size interaction to the model
and test both of the interaction terms with a nested test;
Proc reg data=Userdata.homesalesnew2 plots=none;
model  price= size quality qualitysquare DummyB DummyC DummyBSize DummyCSize;
test  DummyBSize, DummyCSize;
run;

*2. Nested F is insignificant, remove from model and refit;
Proc reg data=Userdata.homesalesnew2 plots=none;
model  price= size quality qualitysquare DummyB DummyC;
run;

/*  */
/*  */
/* Continue with this model for 
assessing and use for prediciton or estimation */
/*  */
/*  */

/*  */
/*  */
/* Beyond Recorded Lecture */
/*  */
/*  */

*Confidence interval for the betas: add /clb to model statement;
proc reg data=Userdata.homesalesnew2 plots=none;
model price = size quality qualitysquare dummyb dummyc/clb;
run;

*Interval estimate for homes that are 1500 square feet, 
quality rating of 8 and in school district A;

data homepre;
input  price size quality qualitysquare DummyB DummyC;
*instead of writing each variable, you can go to the library and drag the names;
cards; *you always need this statement when you write your own table;
. 15 8 64 0 0
;
run;

data Userdata.homesalespredfull;
set Userdata.homesalesnew2 homepre;
run;

*95% Prediction interval for the value of y: add /cli to model statement;
proc reg data=Userdata.homesalespredfull plots=none; *change data name to new table;
model price = size quality qualitysquare dummyb dummyc/cli;
run;

*95% Confidence interval for the mean value of y: add /clm to model statement;
proc reg data=Userdata.homesalespredfull plots=none; *change data name to new table;
model price = size quality qualitysquare dummyb dummyc/clm;
run;

*98% Confidence interval for the mean value of y: add /clm to model statement;
proc reg data=Userdata.homesalespredfull plots=none; *change data name to new table;
model price = size quality qualitysquare dummyb dummyc/clm alpha=0.02;
run;


/* Classwork Engine Example */
*Refit the model;
data mydata.gasturbine ; *create a new data set saved to your library called homesales2;
	set ourDATA.gasturbine; *set with the original table ;
	rpmsquare=rpm**2;* a double asterik is the ^ in SAS;
	cpratiosquare=cpratio**2;
	rpmcpratio=rpm*cpratio;
	X1=0; *create a varaible called DummyB where every observation will have a value of 0;
	X2=0; *create a varaible called DummyC where every observation will have a value of 0;
	if  engine = 'Traditional' then X1=1; *if the group is B, then the dummy var will recode to 1;
	if engine ='Advanced' then X2=1; *similarly to above;
run;

proc reg data=mydata.gasturbine plots=none;
model heatrate = rpm cpratio rpmcpratio rpmsquare cpratiosquare x1 x2;
run;

/* Nested F Test */
Proc reg data=mydata.gasturbine plots=none;
model  heatrate= rpm cpratio rpmcpratio rpmsquare cpratiosquare x1 x2;
test  X1, X2;
run;















