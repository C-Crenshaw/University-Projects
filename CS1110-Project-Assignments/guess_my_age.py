# PA 02 : Guess My Age
# Carson Crenshaw (cgc8gdt)

# input values
number = input("Pick a number between 1 and 10: ")
birthday = input("If you've already had a birthday this year, enter 1772. Otherwise, enter 1771: ")
year = input("Enter the year that you were born: ")

# calculate values
int(number)
multiply = int(number) * 2
add = int(multiply) + 5
multiply2 = int(add) * 50
trick = int(multiply2) + int(birthday)
subtract = int(trick) - int(year)

# drops the first digit, results in the age of the individual (remainder)
finalyear = subtract % 100

# output
print("The magic number is \"" + str(subtract) + "\". " "That means you are " + str(finalyear) + "!")
