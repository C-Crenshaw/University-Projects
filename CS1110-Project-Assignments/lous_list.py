# PA10: Lous-List
# Carson Crenshaw
# cgc8gdt

import urllib.request

# Function 1: Lectures by A Specific Instructor
def instructor_lectures(department, instructor):
    """
    This function will output all the unique lectures a given professor teaches.
    :param department: The university department of interest.
    :param instructor: The name of the professor of interest.
    :return: A list of all the course names for the lectures (not laboratories, discussions, etc.) taught by a given instructor (within the given department).
    """
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + department
    f = urllib.request.urlopen(url)

    lectures = []

    for text in f:
        text = text.decode('utf-8')
        striplist = text.strip('\n')
        str(striplist)
        coursestring = striplist.split('|')
        if coursestring[3] not in lectures:
            if coursestring[5] == "Lecture":
                if instructor == str(coursestring[4].split('+')[0]):
                    lectures.append(coursestring[3])
    return lectures

# Function 2: Finding Compatible Classes
def compatible_classes(first_class, second_class, needs_open_space=False):
    """
    This function will output whether two classes are compatible and whether either of the classes is at maximum capacity (needs open space).
    :param first_class: A string denoting the first class of interest.
    :param second_class: A string denoting the second class of interest.
    :param needs_open_space: A boolean value (default = False) which notes whether there is space in the class for an additional student.
    :return: A boolean value specifying whether or not two classes can fit into the same schedule (whether or not they are reasonably compatible).
    """
    # Cleaning Data
    list1 = first_class.replace('-', ' ')
    class1 = list1.split(' ')
    list2 = second_class.replace('-', ' ')
    class2 = list2.split(' ')

    classes = []

    # Information for Class #1
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + class1[0]
    f = urllib.request.urlopen(url)
    for text in f:
        text = text.decode('utf-8')
        striplist = text.strip('\n')
        str(striplist)
        coursestring = striplist.split('|')
        if coursestring[1] == class1[1] and coursestring[2] == class1[2]:
                classes.append(coursestring)

    # Information for Class #2
    url = 'http://arcanum.cs.virginia.edu/cs1110/files/louslist/' + class2[0]
    f = urllib.request.urlopen(url)
    for text in f:
        text = text.decode('utf-8')
        striplist = text.strip('\n')
        str(striplist)
        coursestring = striplist.split('|')
        if coursestring[1] == class2[1] and coursestring[2] == class2[2]:
                classes.append(coursestring)

    # Checking Compatibility
    # Whether or not the class is full
    if needs_open_space == True:
        if int(classes[0][15]) >= int(classes[0][16]) or int(classes[1][15]) >= int(classes[1][16]):
            return False
        else:
            return True
    # Mon/Wed/Fri Classes
    elif classes[0][7] == classes[1][7]:
        if classes[0][12] <= classes[1][13] and classes[1][12] <= classes[0][13]:
            return False
        else:
            return True
    # Tues/Thurs Classes
    elif classes[0][8] == classes[1][8]:
        if classes[0][12] <= classes[1][13] and classes[1][12] <= classes[0][13]:
            return False
        else:
            return True
    else:
        return True