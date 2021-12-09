

import math
def total(values):
    total = 0
    for val in values:
        total += float(val)
    return total

def average(values):
    if len(values) == 0:
        return math.nan
    total = 0
    for val in values:
        total += float(val)
    return total / float(len(values))

def median(values):
    if len(values) == 0:
        raise ValueError
    values.sort()
    len_t = len(values)
    if len_t % 2 == 0:
        # Total number of values is even
        first = values[len_t // 2]
        second = values[len_t // 2 - 1]
        return (first + second) / 2
    else:
        return values[len_t //2]
