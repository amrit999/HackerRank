# jumpingOnClouds has the following parameter(s):
# int c[n]: an array of binary integers
# Returns --> int: the minimum number of jumps required

def jumpingOnClouds(c):
    jump = 0
    index = 0
    while index < len(c) - 2:
        if c[index + 2] == 0:
            jump += 1
            index = index + 2

        elif c[index + 1] == 0:
            jump += 1
            index = index + 1
    if index == len(c) - 2:
        jump += 1

    return jump
