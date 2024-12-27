
def rodCutting(arr, n):
    revenue = [0]
    for i in range(len(arr)):
        for j in range(i):
            revenue[i] = revenue[j] + rodCutting(arr, i - j)
    return revenue[-1]