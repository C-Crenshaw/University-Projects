*========================================================;
*========================================================;
*     Tattoos        ;
*========================================================;
*========================================================;
  *Fit the logistic regression model;
  proc logistic data=ourdata.tattoos;
 model removal(event='1') =  depth gender method;
 *we want to specify the success in the event = option;
 run;
 
 *========================================================;
*========================================================;
*     SIRDS        ;
*========================================================;
*========================================================;
 
   proc logistic data=ourdata.sirds;
 model survival (event='1')= birthweight;
 *we want to specify the success in the event = option;
 run;
 
    proc logistic data=ourdata.sirds;
 model survival (event='1')= birthweight/expb;
 *we can use the /expb option in the model statement
 to have sas calculate e^betai;
 run;

    proc logistic data=ourdata.sirds;
 model survival (event='1')= birthweight/alpha=0.02;
 *as usual, we can add an alpha option to change the level of significance;
 run;
