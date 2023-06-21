/* Question 1 */
proc sgscatter data= OURDATA.NBADATA;
 title "Average Resale Value X Scatter Plots"; 
plot  AvgResale*( AvgPrice Payroll Hotdog Beer Parking SRS19 Attend19 );
* plot Y*(x1 x2 x3...);
run;
title;

/* Question 2 */
proc sgplot data=ourDATA.NBADATA;
	vbox AvgResale / category=Conference ;
	*vbox RESPONSE /category=QUALITATIVE;
run;

proc sgplot data=ourDATA.NBADATA;
	vbox AvgResale / category=Playoffs19 ;
	*vbox RESPONSE /category=QUALITATIVE;
run;

/* Question 3 */
proc sgplot data=ourdata.NBADATA;
vline Playoffs19/response=AvgResale group=Conference stat=mean datalabel;
run;

/* Question 4 */
proc sgplot data=ourdata.NBADATA;
reg x=AvgPrice y=AvgResale/group=Playoffs19;
run;

proc sgplot data=ourdata.NBADATA;
reg x=AvgPrice y=AvgResale/group=Conference;
run;

/* Question 5 */
proc reg data=ourdata.NBADATA plots=none;
model AvgResale=AvgPrice Payroll Hotdog;
run;

/* Question 8 */
data mydata.nba2; 
     set ourdata.nbadata; 
     DumCon=0; 
     if conference= 'E'  then dumcon=1; 
     DumPlay=0; 
     if playoffs19= 'Yes' then dumplay=1; 
     Qualint=DumCon*DumPlay;
run;

proc reg data=mydata.nba2;
model  AvgResale=AvgPrice Payroll Hotdog DumCon DumPlay Qualint;
run;

/* Question 9 */
Proc reg data=mydata.nba2 plots=none;
model  AvgResale= AvgPrice Payroll Hotdog DumCon DumPlay Qualint;
test  Qualint;
run;

/* Question 10 and 11 */
data mydata.nba3; 
     set mydata.nba2; 
     PriceConf= AvgPrice*DumCon; 
run; 

proc reg data=mydata.nba3;
model  AvgResale=AvgPrice Payroll Hotdog DumCon DumPlay Qualint PriceConf;
test  PriceConf;
run;








