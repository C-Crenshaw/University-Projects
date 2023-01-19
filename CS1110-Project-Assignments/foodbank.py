# Carson Crenshaw
# cgc8gdt
# At-Home Coding Exercise 5

def maxServed(fptr, year, served):
    """
    This function should output a single locality from the csv file according to the appropriate parameters.
    :param fptr: A file handle (fptr) which is positioned at the beginning of a csv file (Food_Bank_Data.csv). The contents of Food_Bank_Data.csv represents the donations and population served by the localities as reported by Federation of Virginia Food Banks.
    :param year: An integer value that is a specific year.
    :param served: An integer value served which represents the following: 0 – find the locality of the maximum number of households served; 1 – find the locality of the maximum number of individuals served; or 2 – find the locality of the maximum number of children served.
    :return: A string which is the locality of the maximum number served, based on the value of the served parameter.
    """
    # Open file
    filename = 'Food_Bank_Data.csv'
    fptr = open(filename, mode='r')

    # Create a list of lists with all the necessary information
    foodbank = []
    with open(filename) as connection:
        strings = filename.strip().split('\n')
        for line in connection:
            words = line.split(',')
            foodbank.append([words[2], words[0], words[3], words[4], words[6]])
        del foodbank[0]

    # Change numerical values into floats, change empty values to 0
    for list in foodbank:
        list[1] = int(list[1])
        if list[2] == '':
            list[2] = 0
        else:
            list[2] = float(list[2])
        if list[3] == '':
            list[3] = 0
        else:
            list[3] = float(list[3])
        if list[4] == '':
            list[4] = 0
        else:
            list[4] = float(list[4])

    # Sort foodbank entries by year
    foodbankyear = []
    for list in foodbank:
        if list[1] == year:
            foodbankyear.append(list)

    # If the user given an invalid year date that is not included in the dataset, return warning
    if foodbankyear == []:
        return ""

    # Return appropriate max information depending on parameters
    elif served == 0:
        households = []
        for list in foodbankyear:
            households.append([list[2], list[0]])
        households.sort(reverse=True)
        return households[0][1]

    elif served == 1:
        individuals = []
        for list in foodbankyear:
            individuals.append([list[3], list[0]])
        individuals.sort(reverse=True)
        return individuals[0][1]

    elif served == 2:
        children = []
        for list in foodbankyear:
            children.append([list[4], list[0]])
        children.sort(reverse=True)
        return children[0][1]