# Print the largest (maximum) hourglass sum found in arr.
# hourglassSum has the following parameter(s):
# int arr[6][6]: an array of integers
# returns --> int: the maximum hourglass sum
# Constraints : element of array range between vale -9 to 9


def hourglassSum(arr):
    my_sum = 0
    max_sum = -63
    for i in range(0, 4):
        for j in range(0, 4):
            my_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                     arr[i + 2][j + 2]

            if my_sum > max_sum:
                max_sum = my_sum
    return max_sum   