# There is a string, , of lowercase English letters that is repeated infinitely many times.
# Given an integer, find and print the number of letter a's in the first letters of the infinite string.

# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider
# Returns --> int: the frequency of a in the substring

def repeatedString(s, n):
    # Write your code here
    r = n % len(s)
    q = n // len(s)
    occurance = (q * s.count('a')) + s.count('a', 0, r)
    return occurance
