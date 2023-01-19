# PA05: Pocket Calculator
# Carson Crenshaw (cgc8gdt)

# Defining Global Variables
currentval = 0
recentoperation = " "
recentargument = int(currentval)
seriesofop = str(currentval)


# Function 1: Get Value
def get_value():
    """
    A function which returns the current value of the calculator (no change to global variables).
    :return: The int representing the current value stored in the calculator.
    """
    return currentval


# Function 2: Clear
def clear(intarg=0):
    """
    A function which resets the second and third globals mentioned above (recentoperation and recentargument) to their initial values, sets the first and fourth globals mentioned above (currentval and seriesofop) to the argument’s int value and its str representation, respectively, and returns the current int value.
    :param intarg: An optional int argument which defaults to 0.
    :return: Current int value.
    """
    global recentoperation, recentargument, currentval, seriesofop
    recentoperation = " "
    recentargument = int(currentval)
    currentval = intarg
    seriesofop = str(currentval)

    return currentval


# Function 3: Step
def step(operator, intarg2):
    """
    A function which enacts a single calculation step by updating the calculator’s global variables to reflect the operation involved.
    :param operator: A string arithmetic operator ("+", "-", "*", or "//").
    :param intarg2: An int argument (addend, subtrahend, factor, or divisor) to the previous operator.
    :return: The calculator’s current int value.
    """
    global recentoperation, recentargument, seriesofop, currentval
    recentoperation = operator

    recentargument = intarg2

    seriesofop = "(" + str(seriesofop) + ")" + str(recentoperation) + str(recentargument)

    # Actual calculations occur in this conditional
    if operator == "+":
        currentval = int(currentval) + int(recentargument)
    elif operator == "-":
        currentval = int(currentval) - int(recentargument)
    elif operator == "//":
        currentval = int(currentval) // int(recentargument)
    else:
        currentval = int(currentval) * int(recentargument)

    return currentval


# Function 4: Repeat
def repeat():
    """
    A function which causes the calculator to repeat its last calculation step using the implementation of the step() function.
    :return: The calculator’s current int value. If no previous operation has been recorded, the function will return the current int value.
    """
    global recentoperation, recentargument, seriesofop, currentval
    if recentoperation == " ":
        currentval = currentval
    else:
        currentval = step(recentoperation, recentargument)
    return currentval


# Function 5: Get Expression
def get_expr():
    """
    A function which will produce the complete expression calculated. The program already stores and updates the current expression in the desired format as the fourth global variable above (seriesofop), so the function return this stored variable in the implementation of get_expr().
    :return: A string representing the current expression.
    """
    global seriesofop
    return seriesofop

step1 = step("+", 3)
print(get_expr(), "=", step1)
step2 = step("-", 1)
print(get_expr(), "=", step2)