*========================================================;
*========================================================;
*              Gasturbine           ;
*========================================================;
*========================================================;

proc reg data=ourdata.gasturbine1 plots(only)=(residualbypredicted 
residualplot qqplot residualhistogram);
model heatrate=rpm cpratio rpmcpratio/dwprob;
run;

*========================================================;
*========================================================;
*              Street Vendor           ;
*========================================================;
*========================================================;

proc reg data=ourdata.streetven2 plots(only)=(residualbypredicted 
residualplot qqplot residualhistogram);
model earnings= age hours int/dwprob;
run;

data mydata.updatesv;
set ourdata.streetven2;
lny=log(earnings);
sqrty=sqrt(earnings);
invy=1/earnings;
run;

proc reg data=mydata.updatesv plots(only)=(residualbypredicted 
residualplot qqplot residualhistogram);
original: model earnings=age hours int;
log: model lny=age hours int/dwprob; 
square_root: model sqrty=age hours int/dwprob; 
inverse: model invy=age hours int/dwprob; 
run;

Proc reg data=mydata.updatesv plots=none;
original: model earnings=age hours int/cli;
square_root: model sqrty=age hours int/cli; 
run;


/* Classwork Example: Homesales */
proc reg data=ourdata.homesalesnew plots(only)=(residualbypredicted 
residualplot qqplot residualhistogram);
model price= size quality qualitysquare DummyB DummyC/dwprob;
run;














