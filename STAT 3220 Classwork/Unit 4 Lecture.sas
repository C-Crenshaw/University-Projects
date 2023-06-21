*========================================================;
*========================================================;
*    Pre Recorded   4.1    ;
*========================================================;
*========================================================;
*========================================================;
*========================================================;
*     Discrimination        ;
*========================================================;
*========================================================;

*Suppose you are investigating allegations of gender 
discrimination in the hiring practices of a particular firm.
 An equal-rights group claims that females are less likely 
 to be hired than males with the same background , 
 experience, and other qualifications. Data were collected 
 from 28 former applicants on the following variables: x_1= 
 Years of higher education (2, 6, or 8), x_2= Years of 
 experience x_3= 1 if male, 0 if female. The response 
 variable is an indicator of whether the applicant was hired: 
 y=1 if hired, 0 if not.;
 

 *========================================================;
 *QUESTION: Fit the logistic Regression Model;
 
 proc logistic data=ourdata.discrim;
 model hire =educ exp gender;
 run;
 
 
 *NOTE: In the output, Probability modeled is HIRE=0. 
 We want pi= P(y=1), so we need to tell SAS that 1
 is the event that is a success.;
 
 proc logistic data=ourdata.discrim;
 model hire (event='1')= educ exp gender;
 run;
 
 *It is probably wise to just always tell SAS what the event
 of a success is. NOTE also, you can have your response 
 as a string and you would just write event = "YES" 
 or whatever the success was.;
 
 
  *========================================================;
 *QUESTION: Calculate the Percentage change in odds between 
 males and females;
 
 
 *We can use a data step or regular calculator to calculate this;
 data calc;
 ebeta= exp(5.6037);
 est= exp(5.6037)-1;
 run;
 
 *or, even easier, we can use the /expb option in the model statement
 to have sas calculate e^betai;
  proc logistic data=ourdata.discrim;
 model hire (event='1')=educ exp gender/expb;
 run;
 
 
  *========================================================;
 *QUESTION: Calculate a 95% confindence interval for the mean response E(y)
 when x1=4, x2=0, and x3=1;
 
 *as always, we create a data table with a new observation missing y;
 data new;
 input HIRE EDUC EXP GENDER;
cards;
. 4 0 1
. 4 0 0
;
run;


*add it to the original data table;
data mydata.discrim2;
set ourdata.discrim new;
run;
 
 *Unfortunately, there is not a very good equivalent to the /cli
 option for proc reg, so we will use the output statement to store our 
 predictions and confidence intervals;
 proc logistic data=mydata.discrim2;
 model hire (event='1')=educ exp gender;
 output out=pred p=phat lower=lcl upper=ucl;

*The pred table is created, but it is easier to view if we print it.;
proc print data=pred;
run;


*========================================================;
*========================================================;
*     Pre-Recorded Lecture  4.2      ;
*========================================================;
*========================================================;
*========================================================;
*========================================================;
*     Discrimination        ;
*========================================================;
*========================================================; 
 *========================================================;
 *QUESTION: Are the variables related to experience (x1 and x2)
 significant predictors of hiring status?;



*Complete model;
proc logistic data=ourdata.discrim;
 model hire (event='1')=educ exp gender;
run;


*Reduced model;
proc logistic data=ourdata.discrim;
 model hire (event='1')=gender;
run;



*Create a data table to calculate and storethe statistic, 
pvalue and critical value;

data calc;
nestedstat= 20.4299-2.2078; *calculates the test statistic;
df=3-1; *calculates the DF;
nestedcrit= quantile('chisquare',.95,df); *computes the rejection region;
nestedpvalue= sdf('chisquare',nestedstat,df); *calculates the p-value of the test statistic;
*print the above quantities;
proc print data=calc;
run;

*NOTE: When we use the test statement, a the same nested test is performed
but used a different statistic. So we will NOT use it.;
 
 proc logistic data=ourdata.discrim;
 model hire (event='1')=educ exp gender;
test educ,exp; *WE WILL NOT USE THIS (see note above);
run;


*========================================================;
*========================================================;
*     Discrimination        ;
*========================================================;
*========================================================;
  proc logistic data=ourdata.discrim plots(only label)=(influence leverage dpc);
 model hire (event='1')=educ exp gender/lackfit aggregate scale=none;
run;

*========================================================;
*========================================================;
*     Unit 4.3      ;
*========================================================;
*========================================================;



*========================================================;

*QUESTION: Is there evidence of differences among the mean
sorption rates of the three organic solvent types?;

*Just as plotting a categorical variable for regression
we can look at the plot of means;
proc sgplot data=ourdata.sorprate;
 vline solvent /response=rate stat=mean markers datalabel;
run;

*But, to get a better idea of the within sample variation
we can look at boxplots;
proc sgplot data=ourdata.sorprate;
vbox rate/ category=solvent;
run;


*========================================================;

*QUESTION: Test is there is a statistical difference between
the three means.;

*We can do this the way we've learned through the Regression method
where we just have categorical variables in the model;
*chose esters as base level;
data mydata.sorprate2;
set ourdata.sorprate;
aroma=0;
chloro=0;
if solvent='1' then aroma=1;
if solvent='2' then chloro=1;
run;

proc reg data=mydata.sorprate2 plots=none;
model rate=aroma chloro;
run;


*However, it is much easier to employ the identical Computation method
using proc anova;
proc anova data=ourdata.sorprate;
class solvent; *defines the categorical variable;
model rate=solvent;
run;




*========================================================;
*========================================================;
*     Two Factor     ;
*========================================================;
*========================================================;

*========================================================;

*QUESTION: Is there evidence of an interaction 
between Class Standing and Exam Preparation?;

proc sgplot data=ourdata.examprep;
 vline prep /response=rating group=standing 
 stat=mean markers datalabel;
run;

proc sgplot data=ourdata.examprep;
 vline standing /response=rating group=prep 
 stat=mean markers datalabel;
run;


*========================================================;

*QUESTION: Test to see if the interaction is significant. 
How should you proceed?;

*We can model this using the Regression Approach with 
two categorial variables and interactions. 
then a nested F test on the 
interaction;
data mydata.examprep2;
set ourdata.examprep;
classM=0;
if standing ='MED' then classM=1;
classH=0;
if standing ='HI' then classH=1;
prepP=0;
if prep='PRACTICE' then prepP=1;
MP=classM*PrepP;
HP=classH*PrepP;
run;

proc reg data=mydata.examprep2 plots=none;
model rating= classm classh prepp mp hp;
test mp,hp;
run;

*Computation method;
proc anova data=ourdata.examprep;
class standing prep; *put both main effects;
model rating=standing prep standing*prep;
 *include main effects and interaction;
run;

*The interaction is not significant.  We will remove it and 
compare the means within main effects;
proc anova data=ourdata.examprep;
class standing prep;
model rating=standing prep;
run;



*QUESTION: Is there evidence of an interaction 
between Class Standing and Exam Preparation?;

proc sgplot data=ourdata.examprep;
 vline prep /response=rating group=standing 
 stat=mean markers datalabel;
run;

proc sgplot data=ourdata.examprep;
 vline standing /response=rating group=prep 
 stat=mean markers datalabel;
run;


*========================================================;

*QUESTION: Test to see if the interaction is significant. 
How should you proceed?;

*We can model this using the Regression Approach with 
two categorial variables and interactions. 
then a nested F test on the 
interaction;
data mydata.examprep2;
set ourdata.examprep;
classM=0;
if standing ='MED' then classM=1;
classH=0;
if standing ='HI' then classH=1;
prepP=0;
if prep='PRACTICE' then prepP=1;
MP=classM*PrepP;
HP=classH*PrepP;
run;

proc reg data=mydata.examprep2 plots=none;
model rating= classm classh prepp mp hp;
test mp,hp;
run;

*Computation method;
proc anova data=ourdata.examprep;
class standing prep; *put both main effects;
model rating=standing prep standing*prep;
 *include main effects and interaction;
run;

*The interaction is not significant.  We will remove it and 
compare the means within main effects;
proc anova data=ourdata.examprep;
class standing prep;
model rating=standing prep;
run;




*========================================================;
*========================================================;
*     Unit 4.4      ;
*========================================================;
*========================================================;
*========================================================;

*QUESTION: Determine the pairs of solvent types that are 
significantly different. Use an experiment error rate of 0.05;

proc anova data=ourdata.drinkers;
class grp;
model score=grp;
means grp/ tukey lines;
run;

data criticaldiff;
w=3.79069*(0.175480/sqrt(11));
proc print data=criticaldiff;
run;


*========================================================;

*QUESTION: Use an experiment error rate of 0.025. What changes?;

proc anova data=ourdata.drinkers;
class grp;
model score=grp;
means grp/ tukey lines alpha=0.025;
run;

data criticaldiff;
w=4.19634*(0.175480/sqrt(11));
proc print data=criticaldiff;
run;



*========================================================;

*QUESTION: Do these data violate the assumptions of ANOVA?;

*1. Populations for EACH TREATMENT are normal;

*Histogram of each treatment;

proc sgpanel data=ourdata.drinkers;
panelby grp;
histogram score;
density score /type=normal;
run;

*There are too few of observations, let's look at all of the data;

proc sgplot data=ourdata.drinkers;
histogram score;
density score /type=normal;
run;


*2. Population variances of treatments are equal;

*Boxplot;
proc sgplot data=ourdata.drinkers;
vbox score/ category=grp;
run;

*levene's test (non-normal);
proc anova data=ourdata.drinkers;
class grp;
model score=grp;
means grp/ hovtest=levene(type=abs);
run;

