

/* MODULE ONE: ESSENTIALS */


*Data functions manipulate information like subsetting, aggregated attributes, setting flags, etc., 
while on the other hand a proc step is like a procedure that you want to perform on the data;
/* *EXAMPLE */

data mycars;
	set sashelp.cars;
	AvgMPG=mean(mpg_city, mpg_highway);
run;

*title "Cars with Average MPG Over 35";

proc print data=mycars;
	var make model type avgmpg;
	*where AvgMPG > 35;
run;

title "Average MPG by Car Type";

proc means data=mycars mean min max maxdec=1;
	var avgmpg;
	class type;
RUN;

TITLE;
*Global statement outside of classic steps within data or proc functions, other gs include options and libname;


/* MODULE TWO: ACCESSING DATA */


*Work library - personal temporary tables, Sashelp library - sample tables                      *;
*WORK is the default library
/* *EXAMPLE; */

proc contents data=work.class;
	*OR;

proc contents data=class;

*Creating a Library to store data from a previously created folder EXAMPLE;
libname out "/home/u62112051/EPG1V2/output";

data out.class_copy1 out.class_copy2;
	set sashelp.class;
run;

/* *Using a Library to Read Excel Sheets EXAMPLE; */
*Complete the OPTIONS statement;
options validvarname=v7;
*Complete the LIBNAME statement;
libname xlstorm xlsx "/home/u62112051/EPG1V2/data/storm.xlsx";
*Complete the DATA= option to reference the STORM_SUMMARY worksheet;

proc contents data=xlstorm.storm_summary;
run;

*Clear the XLSTORM library;
libname xlstorm clear;

/* *Importing and Using a CSV File EXAMPLE; */

PROC IMPORT DATAFILE="path/filename.csv" DBMS=CSV OUT=output-table <REPLACE>;
	<GUESSINGROWS=n|MAX>;
RUN;
*Note: You can also use the import strategy to import and use excel files;


/* MODULE THREE: EXPLORING AND VALIDATING DATA */


*Library referenced in this code;
libname pg1 "/home/u62112051/EPG1V2/data";

/* *Print Command (first ten rows) EXAMPLE; */
proc print data=pg1.storm_summary (obs=10);
	var Season Name Basin MaxWindMPH MinPressure StartDate EndDate;
run;

/* *Calculating Summary Statistics EXAMPLE; */
proc means data=pg1.storm_summary;
	var MaxWindMPH MinPressure;
run;

/* *Examine extreme values EXAMPLE */
proc univariate data=pg1.storm_summary;
	var MaxWindMPH MinPressure;
run;

/* *List unique values and frequencies EXAMPLE */
proc freq data=pg1.storm_summary;
	tables Basin Type Season;
run;

/* *Filtering Rows EXAMPLES; */
proc print data=pg1.storm_summary;
	*Add WHERE statement;
	where MaxWindMPH >= 156;
run;

proc print data=pg1.storm_summary;
	where Basin = "WP";
run;

proc print data=pg1.storm_summary;
	where Basin in ("SI", "NI");
run;

proc print data=pg1.storm_summary;
	where StartDate >= "01jan2010"d;
run;

proc print data=pg1.storm_summary;
	where Type = "TS" and Hem_EW = "W";
run;

proc print data=pg1.storm_summary;
	where MaxWindMPH>156 or 0<MinPressure<920;
run;
*Note: You can also use special where expressions such as
is missing/is not missing/is null
between/and
like "%"" used for any number of characters/"_" used for single characters

/* Macrovariables EXAMPLE */
%let windspeed = 156;
%let basincode = NA;
%let date = 01jan2000;

proc print data=pg1.storm_summary;
	where MaxWindMPH>=&windspeed and Basin="&basincode" and StartDate>="&date"d;
	var Basin Name StartDate EndDate MaxWindMPH;
run;

proc means data=pg1.storm_summary;
	where MaxWindMPH>=&windspeed and Basin="&basincode" and StartDate>="&date"d;
	var MaxWindMPH MinPressure;
run;

*Second Macrovariable EXAMPLE with "%";
%let ParkCode=YOSE;
%let SpeciesCat=Mammal;

proc freq data=pg1.np_species;
    tables Abundance Conservation_Status;
    where Species_ID like "&ParkCode%" and
          Category="&SpeciesCat";
run;

proc print data=pg1.np_species;
    var Species_ID Category Scientific_Name Common_Names;
    where Species_ID like "&ParkCode%" and
          Category="&SpeciesCat";
run;

/* Formatting Data Values EXAMPLES */
*    Common formats:                                      *;
*       dollar10.2 -> $12,345.67                          *;
*       dollar10.  -> $12,346                             *;
*       comma8.1   -> 9,876.5                             *;
*       date7.     -> 01JAN17                             *;
*       date9.     -> 01JAN2017                           *;
*       mmddyy10.  -> 12/31/2017                          *;
*       ddmmyy8.   -> 31/12/17                            *;
proc print data=pg1.storm_damage;
	format Date MMDDYY10. Cost dollar16.;
run;

proc freq data=pg1.storm_summary order=freq;
	tables StartDate;
	format StartDate MONNAME.;
	*This example sorts the dates by month/groups months together;
run;

/* Sorting Data Values EXAMPLE */
proc sort data=pg1.storm_summary out= storm_sort;
	where Basin in ("NA" "na");
	by descending MaxWindMPH;
run;

/* Identifying and Removing Duplicate Values EXAMPLES */
*	 Removes entirely duplicate rows:                     *;
*    PROC SORT DATA=input-table <OUT=output-table>        *;
*        NODUPKEY <DUPOUT=output-table>;                  *;
*        BY _ALL_;                                        *;
*    RUN;                                                 *;
*                                                         *;
*    Remove duplicate key valuesby specific columns:                         *;
*    PROC SORT DATA=input-table <OUT=output-table>        *;
*        NODUPKEY <DUPOUT=output-table>;                  *;
*        BY <DESCENDING> col-name (s);                    *;
*    RUN;

*Remove duplicates and create a new table, as well as one for the dupes;
proc sort data=pg1.storm_detail out=storm_clean nodupkey dupout=storm_dupes;
	by _all_;
run;
*Create new table for pressure with the following constraints;
proc sort data=pg1.storm_detail out=min_pressure;
	where Pressure is not missing and Name is not missing;
	by descending Season Basin Name Pressure;
run;
*Sort the new pressure table without duplicates;
proc sort data=min_pressure nodupkey;
	by  descending Season Basin Name;
run;


/* MODULE FOUR: PREPARING DATA */


/* Creating New SAS Tables As a Subset of the Data EXAMPLE */
data myclass;
    set sashelp.class;
    where age >= 15;
   	keep name age height;
    drop sex weight;
    format height 4.1 weight 3.;
run;

libname out "/home/u62112051/EPG1V2/demos/p104d07.sas";
*Creates storm cat5 as a permanent table in the output folder using libname;
data out.storm_cat5;
	set pg1.storm_summary;
	where StartDate >= "01jan2000"d and MaxWindMPH>=156;
	keep Season Basin Name Type MaxWindMPH;
	run;

/* Using Expressions to Create New Columns */
data tropical_storm;
	set pg1.storm_summary;
	drop Hem_EW Hem_NS Lat Lon;
	where Type="TS";
	*Two new columns;
	MaxWindKM=MaxWindMPH*1.60934;
	format MaxWindKM 3.;
	StormType="TropicalStorm";
run;

/* Using Numeric Functions to Create New Columns */
data storm_wingavg;
	set pg1.storm_range;
	*Add assignment statements;
	WindAvg = mean(wind1, wind2, wind3, wind4);
	WindRange = Range(wind1, wind2, wind3, wind4);
run;

/* Using Character Functions to Create New Columns */
data storm_new;
	set pg1.storm_summary;
	drop Type Hem_EW Hem_NS MinPressure Lat Lon;
	*Add assignment statements;
	Basin = upcase(basin);
	Name = propcase(name);
	Hemisphere = cats(Hem_NS, Hem_EW);
	Ocean = substr(Basin, 2, 1);
run;

/* Using Date Functions to Create New Columns EXAMPLE */
*  Date function examples:                                *;
*    YEAR (SAS-date)                                      *;
*    MONTH (SAS-date)                                     *;
*    DAY (SAS-date)                                       *;
*    WEEKDAY (SAS-date)                                   *;
*    TODAY ()                                             *;
*    MDY (month, day, year)                               *;
*    YRDIF (startdate, enddate, 'AGE')                    *;
data storm_new;
	set pg1.storm_damage;
	drop Summary;
	*Add assignment and FORMAT statements;
	YearsPassed=yrdif(Date, today(), "age");
	Anniversary=mdy(month(Date), day(Date), year(today()));
	format YearsPassed 4.1 Date Anniversary mmddyy10.;
run;

data eu_occ_total;
	set pg1.eu_occ;
	Year= substr(YearMon, 1, 4);
	Month= substr(YearMon, 6, 2);
	ReportDate= mdy(Month, 1, Year);
	Total=sum(Hotel, ShortStay, Camp);
	format Hotel ShortStay Camp Total comma17. ReportDate monyy7.;
	keep Country Hotel ShortStay Camp ReportDate Total;
	run;
	
/* Conditional Processing with IF-THEN/ELSE EXAMPLES */
data cars2;
    set sashelp.cars;
    if MSRP<20000 then Cost_Group=1;
    else if MSRP<40000 then Cost_Group=2;
    else if MSRP<60000 then Cost_Group=3;
    else Cost_Group=4;
	keep Make Model Type MSRP Cost_Group;
run;

data cars2;
    set sashelp.cars;
    length CarType $ 6;
    if MSRP<60000 then CarType="Basic";
    else CarType="Luxury";
    keep Make Model MSRP CarType;
run;

/* Processing Multiple Statements with IF-THEN/DO EXAMPLES */
data front rear;
    set sashelp.cars;
    if DriveTrain="Front" then do;
        DriveTrain="FWD";
        output front;
    end;
    else if DriveTrain='Rear' then do;
        DriveTrain="RWD";
        output rear;
    end;
run;

data indian atlantic pacific;
	set pg1.storm_summary;
	length Ocean $ 8;
	keep Basin Season Name MaxWindMPH Ocean;
	Basin=upcase(Basin);
	OceanCode=substr(Basin,2,1);
	*Modify the program to use IF-THEN-DO syntax;
	if OceanCode="I" then do;
		Ocean="Indian";
		output indian;
	end;
	else if OceanCode="A" then do;
		Ocean="Atlantic";
		output atlantic;
	end;
	else do;
		Ocean="Pacific";
		output pacific;
	end;
run;


/* MODULE FIVE: ANALYZING AND REPORTING ON DATA */


/* Enchancing Reports with Titles, Footnotes, and Labels */
*Titles and Footnotes;
title1 "Class Report";
title2 "All Students";
footnote1 "Report Generated on 01SEP2018";

proc print data=pg1.class_birthdate;
run;

*Using macro variables;
%let age=13;

title1 "Class Report";
title2 "Age=&age";
footnote1 "Report Generated on %sysfunc(today(),date9.)";

proc print data=pg1.class_birthdate;
	where age=&age;
run;

*Labels;
proc means data=sashelp.cars;
	where type="Sedan";
	var MSRP MPG_Highway;
	label MSRP="Manufacturer Suggested Retail Price"
          MPG_Highway="Highway Miles per Gallon";
run;

*Grouped Report;
proc sort data=sashelp.cars out=cars_sort;
	by Origin;
run;

proc freq data=cars_sort;
	by Origin;
	tables Type;
run;

/* Creating Frequency Reports (and Graphs) */
ods graphics on;
proc freq data=sashelp.heart order=freq nlevels;
	tables Chol_Status / nocum plots=freqplot(orient=horizontal scale=freq);
run; 

*Two-way Frequency Report;
title "Blood Pressure by Cholesterol Status";
proc freq data=sashelp.heart;
	tables BP_Status*Chol_Status;
run; 
title;
*PROC FREQ statement options:
*        NOPRINT                                          
*    TABLES statement options:                           
*        NOROW, NOCOL, NOPERCENT                          
*        CROSSLIST, LIST                               
*        OUT=output-table;     

/* Creating Summary Statistics Reports */
proc means data=pg1.storm_final mean median min max std maxdec=0;
	var MaxWindMPH;
	class BasinName StormType;
	ways 0 1 2;
run;


/* MODULE SIX: EXPORTING RESULTS */


*Using a macrovariable to export data;
proc export data=pg1.storm_final
	outfile = "&outpath/storm_final"
	dbms=csv replace;
run;

*Using an Excel Workbook;
libname myxl xlsx "&outpath/cars.xlsx";

data myxl.asiacars;
    set sashelp.cars;
    where origin='Asia';
run;

libname myxl clear;

*Exporting to Excel Using ODS;
ods excel file= "&outpath/wind.xlsx" style=sasdocprinter
		options(sheet_name="Wind Stats");
title "Wind Statistics by Basin";
ods noproctitle;
proc means data=pg1.storm_final min mean median max maxdec=0;
    class BasinName;
    var MaxWindMPH;
run;

ods excel options(sheet_name="Wind Distribution");
title "Distribution of Maximum Wind";
proc sgplot data=pg1.storm_final;
    histogram MaxWindMPH;
    density MaxWindMPH;
run; 
title;  
ods proctitle;
*Add ODS statement;
ods excel close;

*Exporting to PDF;
ods pdf file="&outpath/wind.pdf" startpage=no style=journal pdftoc=1;
ods noproctitle;

ods proclabel "wind statistics";
title "Wind Statistics by Basin";
proc means data=pg1.storm_final min mean median max maxdec=0;
    class BasinName;
    var MaxWindMPH;
run;

ods proclabel "Wind Distribution";
title "Distribution of Maximum Wind";
proc sgplot data=pg1.storm_final;
    histogram MaxWindMPH;
    density MaxWindMPH;
run; 
title;  

ods proctitle;
ods pdf close;


/* MODULE SEVEN: USING SQL IN SAS */

title "International Storms since 2000";
title2 "Category 5 (Wind>156)";
proc sql;
*Add SELECT statement;
select Season, propcase(Name) as Name, StartDate format=mmddyy10., MaxWindMPH
	from pg1.storm_final
	where MaxWindMPH > 156 and Season > 2000
	order by MaxWindMPH desc, Name;
quit;

title;

*Joining Tables;
proc sql;
select Season, Name, s.Basin, BasinName, MaxWindMPH 
    from pg1.storm_summary as s inner join pg1.storm_basincodes as b
		on upcase(s.Basin)=b.Basin
    order by Season desc, Name;
quit;























