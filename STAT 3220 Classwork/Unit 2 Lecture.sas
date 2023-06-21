*========================================================;
*========================================================;
*                CODE FOR RECORDED LECTURES (Unit 2.2)              ;
*========================================================;
*========================================================;

*========================================================;
*========================================================; 
/* SNOWGEESE EXAMPLE */
*========================================================;
*========================================================; 

*Intraction between ADfiber and diet;
proc sgplot data=ourdata.snowgeese;
scatter y=WtChange x= ADFiber/group= Diet;
run;

*Intraction between ADfiber and diet with regression line;
proc sgplot data=ourdata.snowgeese;
scatter y=WtChange x= ADFiber/group= Diet;
reg y=WtChange x= ADFiber/group= Diet;
run;

*Not really an interaction between DigEff and Diet;
proc sgplot data=ourdata.snowgeese;
scatter y=WtChange x=  DigEff/group= Diet;
reg y=WtChange x= DigEff/group= Diet;
run;

*Create dummy var and interaction;
data mydata.snowgeese1;
set ourdata.snowgeese;
dummyplant=0;
if diet = "Plants" then dummyplant=1;
ADFiberxDummyPlant=ADFiber*DummyPlant;
run;

*Model with interaction;
proc reg data=mydata.snowgeese1;
model wtchange=adfiber dummyplant adfiberxdummyplant;
run;

*Model without interaction;
proc reg data=mydata.snowgeese1;
model wtchange=adfiber dummyplant ;
run;

*========================================================;
*========================================================; 
/* Fuel Example */
*========================================================;
*========================================================; 

/* Interaction Plots */
proc sgplot data=ourdata.diesel;
vline fuel/response=perform group=brand stat=mean datalabel;
run;

proc sgplot data=ourdata.diesel;
 vline brand/response=perform group=fuel stat=mean datalabel;
run;

*create dummy variabels and interactions;
data mydata.diesel1;
set ourdata.diesel;
x1=0;
x2=0;
x3=0;
if fuel = "F2" then x1=1;
if fuel = "F3" then x2=1;
if brand = "B2" then x3=1;
x1x3=x1*x3;
x2x3=x2*x3;
run;


*========================================================;
*========================================================; 
/* Crudeoil example */
*========================================================;
*========================================================; 

*Create dummy var and interaction;
data mydata.crudeoil1;
set ourdata.crudeoil;
Interaction= PRESSURE*  DIPANGLE;
run;

*Model with interaction;
proc reg data=mydata.crudeoil1;
model  OILREC=PRESSURE  DIPANGLE interaction;
run;

*========================================================;
*========================================================;
*              Recorded Lecture     (Unit 2.3)        ;
*========================================================;
*========================================================; 
*========================================================;
*========================================================; 
/* Fuel Example */
*========================================================;
*========================================================; 
*Nested F-test the long way;
proc reg data= ourdata.diesel1 plots=none;
complete: model perform= x1 x2 x3 x1x3 x2x3;
reduced: model perform= x1 x2 x3 ;
run;
data nestedFtest;
Fstat=((1512.41-67.6)/(5-3))/11.278;
pvalue = SDF('F',Fstat,5 - 3 ,12 - 5 - 1); 
Fcritical = quantile('F',.95,5 - 3 ,12 - 5 - 1);
proc print data=nestedFtest;
run;


proc reg data= ourdata.diesel1 plots=none;
complete: model perform= x1 x2 x3 x1x3 x2x3;
test x1x3, x2x3 ;
run;


*========================================================;
*========================================================;
*                HOMESALES                 ;
*========================================================;
*========================================================; 

*EDA;
proc sgscatter data=ourDATA.homesalesnew;
	plot price* (quality size)/columns=1;
run;


proc sgplot data=ourDATA.homesalesnew;
	vline school / response=price datalabel stat=mean;
run;


*create all of the terms we need;
data mydata.homesalesnew1 ; *create a new data set saved to your library called homesales2;
	set ourDATA.homesalesnew; *set with the original table ;
	qualitysquare=quality**2;* a double asterik is the ^ in SAS;
	sizequal=size*quality; *interaction;
	sizequal2=size*qualitysquare; *higher order interaction;
	DummyB=0; *create a varaible called DummyB where every observation will have a value of 0;
	DummyC=0; *create a varaible called DummyC where every observation will have a value of 0;
	if  school = 'B' then DummyB=1; *if the group is B, then the dummy var will recode to 1;
	if school='C' then DummyC=1; *similarly to above;
run;


*STAGE ONE: 1. Fit model with all quant predictors;
proc reg data=mydata.homesalesnew1 plots=none;
model price = size quality qualitysquare sizequal sizequal2;
run;

*STAGE ONE: 2. Global Test is signifiant, test the sizeXqual interaction;
proc reg data=mydata.homesalesnew1 plots=none;
model price = size quality qualitysquare sizequal sizequal2;
test sizequal, sizequal2;
run;

*STAGE ONE: 3. remove interactions and refit;
proc reg data=mydata.homesalesnew1 plots=none;
model price = size quality qualitysquare;
run;

/*  */
/*  */
/* END STAGE ONE: T TEST for Qual^2 is significant. We will move on. */
/*  */
/*  */



*STAGE TWO: Add School District to the model and perform nested F test;
proc reg data=mydata.homesalesnew1 plots=none;
model price = size quality qualitysquare dummyb dummyc;
test dummyb, dummyc;
run;

/*  */
/*  */
/* END STAGE TWO: NESTED F TEST for School District is significant. 
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

proc sgplot data=ourdata.homesalesnew;
scatter x=size y=price/group=school;
reg x=size y=price/group=school;
run;


proc sgplot data=ourdata.homesalesnew;
scatter x=quality y=price/group=school;
reg x=quality y=price/group=school;
run;

/* There appears to be an interaction between School District and Size */
data mydata.homesalesnew2;
set mydata.homesalesnew1;
DummyBSize=DummyB*size;
DummyCSize=DummyC*size;
run;

/*  */
/*  */
/* STAGE THREE */
/*  */
/*  */

*STAGE THREE: Add school X size interaction to the model
and test both of the interaction terms with a nested test;
Proc reg data=mydata.homesalesnew2 plots=none;
model  price= size quality qualitysquare DummyB DummyC DummyBSize DummyCSize;
test  DummyBSize, DummyCSize;
run;

*STAGE THREE: Nested F is insignificant, remove from model and refit;
Proc reg data=mydata.homesalesnew2 plots=none;
model  price= size quality qualitysquare DummyB DummyC;
run;