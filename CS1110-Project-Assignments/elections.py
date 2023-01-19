# PA09: Elections
# Carson Crenshaw
# cgc8gdt

# Global Dictionary
statewinners = {}

def add_state(name, votes):
    """
    This function stores the election results for the given state within the global dict "statewinners."
    :param name:  A string to distinguish this state from others (e.g ”Virginia”).
    :param votes: A dictionary whose keys are the names of each candidate (string) and whose values are the number of votes (int) each candidate received in this state.
    :return: The function will determine the winner of the provided state, and then store the name of the winning candidate in the global dictionary "statewinners." Technically, this function should not return anything.
    """
    global statewinners
    largest = max(votes.values())
    for key, value in votes.items():
        if value == largest:
            winner = key.title()
            statewinners[name] = winner

def winner(college):
    """
    The expected behavior of this function is to read the election results from the global dict and determine the nationwide winner from the information in parameter college.
    :param college: A dictionary whose keys are the names of each state (string) and whose values are the amount of electoral votes (int) the state has.
    :return: The function will determine the nationwide winner of the election.
    """
    global statewinners
    electoralcount = {}

    for state in college:
        if state in statewinners:
            electoralcount[statewinners[state]] = 0

    for state in college:
        if state in statewinners:
            electoralcount[statewinners[state]] += college[state]

    totalvotes = 0
    for candidate in electoralcount:
        totalvotes += electoralcount[candidate]
    majority = totalvotes*0.5

    for candidate in electoralcount:
        if electoralcount[candidate] > majority:
            return candidate
    else:
        return "No Winner"


def clear():
    """
    This function returns the global variable "statewinners" to its initial value.
    :return: Resets any global variable(s) to their initial value(s).
    """
    global statewinners
    statewinners = {}
