# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# This function determines how many pairs of socks with matching colors there are.

# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns
# int: the number of pairs

def sockMerchant(n, ar):

    single_socks = 0
    pile = {}
    for socks in ar:
        if socks not in pile:
            pile[socks] = 1
        else:
            del pile[socks]

    for key,value in pile.items():
        if pile[key] != 0:
            single_socks += value
    return (n - single_socks) // 2