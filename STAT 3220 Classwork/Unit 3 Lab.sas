/* #1 */
proc sgscatter data=ourdata.wine2;
	matrix aroma body clarity flavor oakiness; 
run;

proc corr data=ourdata.wine2 nosimple; 
var aroma body clarity flavor oakiness; 
run;

/* #2 */
proc reg data=ourdata.wine2 plots=none;
model quality = aroma body clarity flavor oakiness  / vif; 
run;

/* #4 */
proc reg data=ourdata.wine2 plots=none;
model quality = aroma body clarity flavor oakiness  / 
selection=stepwise SLentry=0.15 SLstay=0.15 details; 
run;

/* #5 */
proc reg data=ourdata.wine2 plots=none;
model quality = aroma body clarity flavor oakiness  / 
selection=stepwise SLentry=0.05 SLstay=0.05 details; 
run;

/* #8 */
proc reg data=ourdata.wine2;
model quality=flavor aroma oakiness dummyregion1 dummyregion2/dwprob;
run;

/* #9 */
proc reg data=ourdata.wine2 
plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
  *You can select one or all of the plot options;
 model quality=flavor aroma oakiness dummyregion1 dummyregion2/r influence;; 
 *DWPROB option gives Durbin Watson test;
run;

/* #11 */
*Remove aroma and oakiness;
 proc reg data=ourdata.wine2 plots(only label)=(cooksd rstudentbypredicted
rstudentbyleverage residualbypredicted residualplot qqplot 
  residualhistogram); 
model quality=flavor dummyregion1 dummyregion2 / r influence;
run;













