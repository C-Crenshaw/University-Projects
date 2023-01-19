/* Import Generated Code (EXCEL Sheet) */
/* Source File: Final Data.xlsx */

%web_drop_table(PROJECT.COUNTRYGDP);

FILENAME REFFILE '/home/u62112051/Project/Final Data.xlsx';

PROC IMPORT DATAFILE=REFFILE
	DBMS=XLSX
	OUT=PROJECT.COUNTRYGDP (drop= AA AB AC AD O P Q R S T U V W X Y Z);
	GETNAMES=YES;
RUN;

PROC CONTENTS DATA=PROJECT.COUNTRYGDP; RUN;

%web_open_table(PROJECT.COUNTRYGDP);

*Print Summary;
proc print data=project.countrygdp (obs=15);
run;

/* NUMERICAL SUMMARIES */

*Calculating Summary Statistics;
proc means data=project.countrygdp;
run;

*List frequencies/Summary of Qualitative variables (except Country);
proc freq data=project.countrygdp;
	tables GSoD_Index IB_1930 Major_Import_or_Export Member_of_NATO World_Region;
run;

*Correlation of quantitaive variables with the response;
proc corr data=PROJECT.COUNTRYGDP pearson nosimple noprob plots=none;
	var Life_Expectancy;
	with GDP;
run;

*Correlation between all variables, whether pairwise relationships between explanatory variables are strong; 
proc corr data=project.countrygdp nosimple; 
var  Average_Population_Age Exports Imports Life_Expectancy Net_Exports Unemployment_Rate Pop_2020; 
run;


/* GRAPHICAL SUMMARIES */

*Histogram of response variable;
proc sgplot data=project.countrygdp;
title "Histogram of Gross Domestic Product (GDP) Per Capita in USD";
histogram gdp / binwidth= 2500 ;
xaxis label="Gross Domestic Product Per Capita";
run;
title;

*Scatterplots for quant. variable;
proc sgscatter data= project.countrygdp;
 title "Scatterplot of GDP (USD $) and Total Population (2020)"; 
plot  gdp*( Pop_2020  );
run;
title;

proc corr data=PROJECT.COUNTRYGDP pearson nosimple noprob plots=none;
	var Pop_2020;
	with GDP;
run;

*Line Plot and Box Plots;
proc sgplot data=project.countrygdp;
	vline Member_of_NATO / response=gdp datalabel stat=mean;
run;

proc sgplot data=project.countrygdp;
	title "Boxplot of GDP (USD $) and Membership in NATO";
	vbox gdp / category=Member_of_NATO ;
run;

proc sgplot data=project.countrygdp;
	vline IB_1930 / response=gdp datalabel stat=mean;
run;

proc sgplot data=project.countrygdp;
	title "Boxplot of GDP (USD $) and Status of Independence (before 1930)";
	vbox gdp / category=IB_1930 ;
run;

proc sgplot data=project.countrygdp;
	vline Major_Import_or_Export / response=gdp datalabel stat=mean;
run;

proc sgplot data=project.countrygdp;
	vbox gdp / category=Major_Import_or_Export ;
run;

proc sgplot data=project.countrygdp;
	vline GSoD_Index / response=gdp datalabel stat=mean;
run;

proc sgplot data=project.countrygdp;
	vbox gdp / category=GSoD_Index ;
run;

proc sgplot data=project.countrygdp;
	vline World_Region / response=gdp datalabel stat=mean;
run;

proc sgplot data=project.countrygdp;
	title "Boxplot of GDP (USD $) and World Region";
	vbox gdp / category=World_Region ;
run;

*Interactions;
proc sgplot data=project.countrygdp;
vline GSoD_Index/response=gdp group=Member_of_NATO stat=mean datalabel;
run;







