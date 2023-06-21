*========================================================;
*========================================================;
*     Drinkers      ;
*========================================================;
*========================================================;


*========================================================;

*QUESTION: Is there evidence of differences among the mean
task score of the four groups?;


proc sgplot data=ourdata.drinkers;
vbox score/ category=grp ;
run;


*========================================================;

*QUESTION: Test is there is a statistical difference between
the three means.;

*Computation method;
proc anova data=ourdata.drinkers;
class grp;
model score=grp;
run;


*========================================================;

*QUESTION: The question of interest is: Does coffee or some other 
form of stimulation really allow a person suffering from 
alcohol intoxication to "sober up"? What is your conclusion?
Include any relevant inferences and confidence intervals. Use alpha=0.05. ;

proc anova data=ourdata.drinkers;
class grp;
model score=grp;
means grp/ tukey cldiff ;
run;

*========================================================;
*========================================================;
*     Tin Lead       ;
*========================================================;
*========================================================;

*QUESTION: Is there evidence of an interaction? ;

proc sgplot data=ourdata.tinlead  ;
 vline method /response=strength group=antimony  
 stat=mean markers datalabel  ;
run;

*QUESTION:	Test if there is statistical 
evidence of an interaction. ;

*Computation method;
proc anova data=ourdata.tinlead;
class antimony method; *put both main effects;
model strength=antimony method antimony*method;
 *include main effects and interaction;
run;

*QUESTION:	Test the main effects. ;
proc sgplot data=ourdata.tinlead;
vbox strength/ category=antimony;
run;

proc sgplot data=ourdata.tinlead;
vbox strength/ category=method;
run;

*Remove the interactions;
proc anova data=ourdata.tinlead;
class antimony method; *put both main effects;
model strength=antimony method;
 *include main effects ;
run;


/* Classwork */
proc anova data=ourdata.eggs2;
class housing wtclass;
model overrun=housing wtclass housing*wtclass;
run;




















