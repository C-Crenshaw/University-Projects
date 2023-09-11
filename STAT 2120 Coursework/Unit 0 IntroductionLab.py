"""""""""""""""""""""""""""""""""""

Introduction lab activity

"""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Python scripts can be commented by starting and ending 
the comment with an odd number of sets of three quotation 
marks. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
A comment using a single set of three quotation marks.
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Using more sets of three quotation marks (as you see 
for all other long comment) is a style choice.

A single-line comment can be started with a # as shown
below. These are typically used for shorter comments.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# A single-line comment.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To read in a data set, a Python package called pandas
first needs to be imported. 

The pd is an abbreviation that we will use in order to 
use a function in that package.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Import required package
import pandas as pd


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To read in a CSV file, the pandas function read_csv()
will be used.

The read_csv() function requires the path to and name of
the data to be read in.

A common convention is to store the path as a variable.

When using the full path as shown below, a 'r' must be
added prior to the starting quotation mark, which 
instructs Python to read the path as it is written 
instead of the default of reading \ as a special character.

If you want to copy a file's path from the file browser, you may use
the following commands:
    1. In MacOS: select the file, then press command+option+C. This will copy the file path to your clipboard.
    2. In Windows: hold shift and then right click the file name. 
       In the menu that appears, you can select 'Copy as Path'
       The file path is now copied to your clipboard. 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Save the path as a variable called 'filename'.
# You can copy your path in the place of the path on the next line.
filename = r"C:/Users/rjr85/Box/stat2120/Rich/Course materials/Data/kickstarter.csv"

# Read in the data at the path saved as 'filename'.
kick_data = pd.read_csv(filename)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To run code, use the series of five buttons above that 
starts with the green arrow. Hovering over each button 
will display its keyboard shortcut.

A #%% breaks a script into independent cells. When the 
cell is run, all of the code in that cell is executed.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#%% Addition Calculations
List = [2, 3] 
sum = sum(List) 
print(sum)
#%%

#%% Another Way to Add 2 and 3
sum = 2 + 3
print(sum)
#%%

#%% Importing the Kickstarter Data
import pandas as pd

filename = r"/Users/CarsonCrenshaw/Documents/STAT 2120 Downloaded Course Materials/kickstarter.csv"

lab_data = pd.read_csv(filename)
#%%