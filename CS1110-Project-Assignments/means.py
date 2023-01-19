# PA08: Means
# Carson Crenshaw
# cgc8gdt

def mean_all(table):
    """
    This function outputs the total average of the entire data table.
    :param table: A list of a list representing a data table.
    :return: The arithmetic mean of all the numbers in the list of lists.
    """
    total = 0
    total_len = 0
    for sub_list in table:
        value = 0
        totalsum = 0
        while value < len(sub_list):
            totalsum = totalsum + sub_list[value]
            value = value + 1
        total += totalsum
        lengthoflist = len(sub_list)
        total_len += lengthoflist
        total_mean = total / total_len
    return total_mean

def mean_by_row(table):
    """
    This function outputs the average for each row of the data table.
    :param table: A “table”, which will be in the form of a list of lists of numbers.
    :return: A list containing the arithmetic means of each row’s values (a “row” is a sublist in the list of lists).
    """
    means_list_row = []
    for sub_list in table:
        value = 0
        sublistsum = 0
        while value < len(sub_list):
            sublistsum = sublistsum + sub_list[value]
            individual_mean = sublistsum / len(sub_list)
            value = value + 1
        means_list_row.append(individual_mean)
    return means_list_row

def mean_by_col(table):
    """
    The function outputs the average for each column of the data table.
    :param table: A “table”, which will be in the form of a list of lists of numbers.
    :return: A list containing the arithmetic means of each column’s values (a “column” is all of the values at a particular index in each of the sublists).
    """
    list_of_col = [] # Create a new list that holds column values and a new list that will hold average values
    average_col = []
    for sub_list in range(len(table[0])):
        list_of_col.append([]) # Creates empty lists for the number of columns
    for sub_lists in table:
        for number in range(len(sub_lists)):
            list_of_col[number].append(sub_lists[number])
    for sub_list in list_of_col: # Repeats row average function; an alternative would be to call the function directly
        value = 0
        colsum = 0
        while value < len(sub_list):
            colsum = colsum + sub_list[value]
            individual_mean = colsum / len(sub_list)
            value = value + 1
        average_col.append(individual_mean)
    return average_col