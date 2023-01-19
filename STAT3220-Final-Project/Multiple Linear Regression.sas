/* Import Generated Code (EXCEL Sheet) */
/* Source File: Final Data.xlsx */

%web_drop_table(MYDATA.COUNTRYGDP);

FILENAME REFFILE '/home/u62112051/Project/Final Data.xlsx';

PROC IMPORT DATAFILE=REFFILE 
	DBMS=XLSX
	OUT=MYDATA.COUNTRYGDP (drop= AA AB AC AD O P Q R S T U V W X Y Z);
	GETNAMES=YES;
RUN;

PROC CONTENTS DATA=MYDATA.COUNTRYGDP; RUN;

%web_open_table(MYDATA.COUNTRYGDP);

*Transform RESPONSE variable using the log function;
data mydata.countrygdp;
set mydata.countrygdp;
lngdp=log(gdp);
run;

proc sgplot data=mydata.countrygdp;
title "Histogram of Gross Domestic Product (GDP) Per Capita in USD with Log Transformation";
histogram lngdp;
xaxis label="Gross Domestic Product Per Capita";
run;
title;

*Dummy Variables for extended model;
data MYDATA.COUNTRYGDP;
set MYDATA.COUNTRYGDP; 
dummyind = 0;
	if  IB_1930 = 'Y' then dummyind = 1;
dummyexport = 0;
	if  Major_Import_or_Export= 'Major Exporter' then dummyexport = 1;
dummyauthor = 0;
dummyhybrid = 0; 
	if  GSoD_Index = 'Authoritarian regime' then dummyauthor = 1;
	if  GSoD_Index = 'Hybrid regime' then dummyhybrid = 1;
dummynato = 0;
	if Member_of_NATO = 'N' then dummynato = 1;
dummyasia = 0; 
dummyafrica = 0;
dummyameri = 0;
dummyeuro = 0;
	if World_Region = 'Asia and the Pacific' then dummyasia = 1;
	if World_Region = 'Africa' then dummyafrica = 1;
	if World_Region = 'Americas' then dummyameri = 1;
	if World_Region = 'Europe' then dummyeuro = 1;
run;

*Initial first model (with all the variables);
proc reg data=MYDATA.countrygdp;
 model lngdp= dummyind dummyexport dummyauthor dummyhybrid dummynato dummyasia dummyafrica dummyameri dummyeuro Pop_2020 Average_Population_Age Life_Expectancy Unemployment_Rate /dwprob;
 run;

*Checking for Multicolinearity;
proc sgscatter data=MYDATA.countrygdp;
	matrix dummyind dummyexport dummyauthor dummyhybrid dummynato dummyasia dummyafrica dummyameri dummyeuro Pop_2020 Average_Population_Age Life_Expectancy Unemployment_Rate;
run;

proc corr data=MYDATA.countrygdp nosimple plots=matrix rank ; 
var Pop_2020 Average_Population_Age Life_Expectancy Unemployment_Rate;
run;

proc reg data=MYDATA.countrygdp plots=none;
model lngdp = Pop_2020 Average_Population_Age Life_Expectancy Unemployment_Rate / vif; 
run;

*Stepwise regression;
proc reg data=MYDATA.countrygdp plots=none;
model lngdp = Pop_2020 Average_Population_Age Life_Expectancy Unemployment_Rate / 
selection=stepwise SLentry=0.15 SLstay=0.15 details; 
run;

*Build Model from Stepwise Regression (only quantitative);
proc reg data=MYDATA.countrygdp;
 model lngdp= Average_Population_Age Life_Expectancy;
 run;

*Adding Dummy Variables to Model (Global F-test);
proc reg data=MYDATA.countrygdp plots = none;
 model lngdp= dummyind dummyexport dummyauthor dummyhybrid dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
 run;

*Individual Beta Test -- remove Independence variable (high p-value);
proc reg data=MYDATA.countrygdp plots = none;
 model lngdp= dummyexport dummyauthor dummyhybrid dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
 run;

*Nested Test -- remove Regime type;
proc reg data=MYDATA.countrygdp plots = none;
 model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
 run; 

proc reg data=MYDATA.countrygdp plots = none;
model lngdp= dummyexport dummyauthor dummyhybrid dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
test dummyauthor, dummyhybrid;
run;

*Nested F-test to check New Variables -- LEAVE IN MODEL;
proc reg data=MYDATA.countrygdp plots=none;
model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
test dummyexport, dummynato, dummyasia, dummyafrica, dummyameri, dummyeuro;
run;

*Check Model Assumptions (Residual Assumptions);
proc reg data=MYDATA.countrygdp plots(only)=(residualbypredicted residualplot qqplot 
  residualhistogram);
 model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy / dwprob;
 run;
 
*Checking for Outliers/Influential Observations;
proc reg data=MYDATA.countrygdp plots(only label)=(cooksd 
 rstudentbypredicted rstudentbyleverage); 
model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy / r influence;
run;

*Remove Outliers;
proc reg data=MYDATA.countrygdp plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy / r influence;
reweight obs.=12;
reweight obs.=54;
reweight obs.=82;
reweight obs.=96;
reweight obs.=102;
reweight obs.=127;
reweight obs.=156;
run;

*Remove Outliers from Dataset;
data MYDATA.countrygdp;
    set MYDATA.countrygdp;
    if Country = "Bahamas" then delete;
    if Country = "Equatorial Guinea" then delete;
    if Country = "Ireland" then delete;
    if Country = "Lebanon" then delete;
    if Country = "Luxembourg" then delete;
    if Country = "Nigeria" then delete;
    if Country = "Singapore" then delete;
run;

proc reg data = MYDATA.countrygdp;
model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy;
run;

*Prediction;
proc reg data=MYDATA.countrygdp plots=none;
model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy / cli;
run;

*External Model Validation;
proc glmselect data=MYDATA.countrygdp;
   partition fraction(test=0.5);
   model lngdp= dummyexport dummynato dummyasia dummyafrica dummyameri dummyeuro Average_Population_Age Life_Expectancy / selection= none;
   output out=outDataForward;
run;

















