# Staircase

# !/bin/python3
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    blank = ' '
    shap = '#'

    for i in range(1, n + 1):
        print((blank * (n - i)) + (shap * i))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)


# Diagonal Difference



import os

def diagonalDifference(arr):
    left = 0
    right = 0
    num = len(arr)
    for i in range(num):
        left = left + arr[i][i]
        right = right + arr[i][num - i - 1]

    result = abs(left - right)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
