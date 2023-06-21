
*========================================================;
*               Navy Fleet                ;
*========================================================;
*========================================================; 


*QUESTION: Does there appear to be a quadratic relationship
between percentage of movement and cost of modifying the fleet?;

proc sgplot data=ourdata.navalbase;
scatter y=percent x=cost;
run;



*========================================================;

*QUESTION: Is the overall model significant? (at alpha =0.1);

data mydata.naval2;
set ourdata.navalbase;
cost2=cost**2; *double asterisk=exponent;
run;

proc reg data=mydata.naval2 plots=none;
model percent= cost cost2;
run;

*========================================================;
*QUESTION: Does there appear to be a  relationship
between percentage of movement and base of the fleet?;


proc sgplot data=ourdata.navalbase;
vbox percent/category=base;
run;

*========================================================;
*QUESTION: Does there appear to be an interaction between
between cost of modifying the fleet and base of the fleet?;


proc sgplot data=ourdata.navalbase;
scatter x=cost y=percent/ group=base;
reg x=cost y=percent / group=base;
run;

*========================================================;
*Consider a complete second order model:
percent = Beta_0 + Beta_1*cost + Beta_2*cost^2 + Beta_3*base
  + Beta_4*cost*base + Beta_4*cost^2*base + e
Fit the model.;


data mydata.naval3;
set mydata.naval2;
basecode = 0;
if base = 'US' then basecode = 1;
costbase= cost*basecode;
cost2base=cost2*basecode;
run;


proc reg data=mydata.naval3 plots=none;
model percent= cost cost2 basecode costbase cost2base;
run;


/* Mexican Street Vendors Classwork */
*Create dummy var and interaction;
data mydata.streetven;
set ourdata.streetven;
Interaction= AGE*  HOURS;
run;

*Model with interaction;
proc reg data=mydata.streetven;
model  EARNINGS=AGE  HOURS interaction;
run;





















