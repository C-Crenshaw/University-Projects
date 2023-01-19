# PA04 Fines
# Carson Crenshaw
# cgc8gdt

# Creating two functions ("fine" and "demerits") which generate how much money and points are charged against drivers who are caught speeding

# Function 1: "Fine"
# Possible charges (for reference):
#   $6 for each mph over the speed limit (no zone)
#   $7 for each mph over (school/work zone)
#   $8 for each mph over AND $200 (residential zone)
#   $350 flat for 20 mph over or higher
#   $30 flat for all speeds 10 mph below

def fine(speed_limit, my_speed, zone=None):
    """
    :param speed_limit: a number that indicates the posted speed limit.
    :param my_speed: a number that indicates the speed that the individual was actually traveling at.
    :param zone: an optional string that indicates what zone the individual is driving in; if not present, it should default to None.
    :return: the fine that the individual will be ticketed with.
    """
    if my_speed - speed_limit >= 20:
        pay = 350
    elif my_speed < speed_limit - 10:
        pay = 30
    elif my_speed > speed_limit and zone == 'school' or zone == 'work':
        pay = int(7 * abs(my_speed - speed_limit))
    elif my_speed > speed_limit and zone == 'residential':
        pay = int(8 * abs(my_speed - speed_limit) + 200)
    elif my_speed > speed_limit:
        pay = int(6 * abs(my_speed - speed_limit))
    else:
        pay = 0
    return pay


# Function 2: "Demerits"
#   3 points for over the speed limit by 1-9 mph
#   4 points for over the speed limit by 10-19 mph
#   6 points for 20+ mph

def demerits(speed_limit, my_speed):
    """
    :param speed_limit: a number that indicates the speed limit that should be driven.
    :param my_speed: a number that indicates the speed that the individual was actually traveling at.
    :return: the number of demerit points earned.
    """
    if my_speed - speed_limit >= 20:
        points = 6
    elif 10 <= my_speed - speed_limit <= 19:
        points = 4
    elif 1 <= my_speed - speed_limit <= 9:
        points = 3
    else:
        points = 0
    return points