# Carson Crenshaw
# cgc8gdt
# At-Home Coding Exercise 2

def quad(x, y):
    """
    Function quad takes as input two decimal values representing an (x, y) point. The program should print the quadrant number for that point.
    :param x: X point value
    :param y: Y point value
    :return: The quadrant that the point resides in. If a point falls on the x-axis or the y-axis, then the function will return 0.
    """
    if x == 0 or y == 0:
        quadrant = 0
    elif x > 0 and y > 0:
        quadrant = 1
    elif  x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    else:
        quadrant = 4
    return quadrant

# Sample Executions
# print(quad(2.0, 3.0))
# 1

#print(quad(-2.0, -3.0))
# 3

#print(quad(2.0, 0.0))
# 0
