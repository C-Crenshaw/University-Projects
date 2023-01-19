# Carson Crenshaw
# cgc8gdt
# At-Home Coding Exercise 3A

# Compare Function
def compare(listofstrings):
    """
    A function which outputs the number of strings where the first and last character are the same, regardless of case
    :param listofstrings: A list of strings
    :return: The number of strings where the first and last character are the same
    """
    # Create a new list to store values that meet the conditional statement
    new_list = []
    for i in listofstrings:
        if i[0].lower() == i[-1].lower():
            new_list.append(i)
    return len(new_list)

