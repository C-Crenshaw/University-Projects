/* Unit 1.0 Classwork */

proc sgplot data=ourdata.sample;
scatter x=footlength y=height;
reg x=footlength y=height;
run;

/* Unit 1.1 Classwork */

/* QUESTION 7: Enter your data */
data GroupEntry;
input name $ footlength height;
cards;
Carson 25.5 69
Maggie 23.5 67
Trinity 25.2 67
Lauren 23 62
Zach 25.9 70
Jenny 23 65
;
run;


/* Highlight all of the lines from data to run above */
/* then select the small run icon in the toolbar.  */


/* QUESTION 7d: Create a Scatter Plot */
proc sgplot data=GroupEntry;
scatter x=footlength y=height;
reg x=footlength y=height;
run;
/* to produce the plot, Highlight the four lines above */
/* then select the small run icon in the toolbar.  */

/* QUESTION 9: Produce Regression Output */
proc reg data=GroupEntry plots=none;
model height=footlength;
run;
/* To produce the output, Highlight the three lines above */
/* then select the small run icon in the toolbar.  */
