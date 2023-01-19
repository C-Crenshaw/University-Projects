# Carson Crenshaw
# cgc8gdt
# This is your starter code for At-Home Coding Exercise 1
# file must be named pennies.py
# The purpose is to write a function that returns the number of pennies (cents) required for change

# Write the num_pennies function here, including docstring:
def num_pennies(itemCost, amtPaid):
    """
    function that returns the number of pennies (cents) required for change
    :param itemCost: how much an item cost (converted within function from dollar amount to pennies)
    :param amtPaid: how much a customer paid (converted within function from dollar amount to pennies)
    :return: the number of pennies (each worth one cent) that will be needed to give change to a customer
    """
    # Convert from a string to a float
    itemCost2 = (float(itemCost) * 100)
    amtPaid2 = (float(amtPaid) * 100)
    # Convert from a float to int
    itemCost2 = int(itemCost2)
    amtPaid2 = int(amtPaid2)
    # Calculate the difference between amount paid and cost
    change = int(amtPaid2 - itemCost2)
    # Number of pennies calculated from remainder after dividing change by 5
    pennyremainder = int((change) % 5)
    pennies = str(pennyremainder)
    return pennies

# main program
# DO NOT EDIT anything after this point
print("This program will calculate the number of pennies required for change.")
itemCost = input("Enter the cost of the item: ")
amtPaid = input("Enter the amount paid: ")
pennies = num_pennies(itemCost, amtPaid)
print("If you paid $" + amtPaid + " for something that costs $" + itemCost + " you will need " + pennies + " pennies." )