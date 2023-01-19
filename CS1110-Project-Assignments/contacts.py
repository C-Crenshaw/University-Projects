# Carson Crenshaw
# cgc8gdt
# At-Home Coding Exercise 4

#Update function
def update(contactDict, list_of_values):
    """
    This function should update a contact dictionary.
    :param contactDict: A dictionary mapping names to email addresses.
    :param list_of_values: A list of tuples consisting of three strings, the first representing the action, the second is a name and the third is an email address.
    :return: The function should process all of the values in the parameter list_of_values to the contactDict dictionary according to the assignment instructions.
    """
    errorcount = 0
    for listtuple in list_of_values:
        if '+' in listtuple:
            if listtuple[1] in contactDict:
                errorcount += 1
            else:
                contactDict[listtuple[1]] = listtuple[2]
        elif '/' in listtuple:
            if listtuple[1] in contactDict:
                contactDict[listtuple[1]] = listtuple[2]
            else:
                errorcount += 1
        elif '-' in listtuple:
            if listtuple[1] in contactDict:
                del contactDict[listtuple[1]]
            else:
                errorcount += 1
        else:
            errorcount += 1
    return errorcount