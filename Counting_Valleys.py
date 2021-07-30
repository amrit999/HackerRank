# countingValleys has the following parameter(s):
# int steps: the number of steps on the hike
# string path: a string describing the path
# Returns --> int: the number of valleys traversed

def countingValleys(steps, path):
    values = {"U": 1, "D": -1}
    level = 0
    count = 0
    for step in path:
        level = level + values[step]
        if (values[step]==1 and level == 0):
            count = count + 1
    return count