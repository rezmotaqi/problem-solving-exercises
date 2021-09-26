def hourglassSum(arr):

    def sum_glass(arr, i, j):
        return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

    best = float("-inf")
    for i in range(4):
        for j in range(4):
            s = sum_glass(arr, i, j)
            if s > best:
                best = s
    return best