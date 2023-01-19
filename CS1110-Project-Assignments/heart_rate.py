# PA03: Heart Rate
# Carson Crenshaw (cgc8gdt)

# Input: The first function calculates the estimated HRmax from the argument 'age'
def gellish2(age):
    """
    Function used to estimate a HRmax formula
    :param age: Age of subject (entered into the function)
    :return: Estimated HRmax in beats per minute (bpm)
    """
    HRmax = 191.5 - (0.007 * age ** 2)
    return float(HRmax)


# Input: Second function calculates whether the heart rate of a given subject falls within the Target Heart Rate (THR) interval
def in_target_range(hr, age):
    """
    Function used to compare heart rate (hr) to THR interval (calculated from 'age' through the gellish2 function)
    :param hr: Heart rate of subject
    :param age: Age of subject
    :return: True if the THR falls in between (or exactly at) 65-85% of the estiamted HRmax, False if it does not
    """
    HRmax2 = gellish2(age)
    THR = .65*HRmax2 <= hr <= .85*HRmax2
    return THR
