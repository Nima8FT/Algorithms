A = [23, 12, 1, 8, 34, 54, 2, 3]

n = len(A)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        key = A[i]
        j = i
        while j >= gap and A[j - gap] > key:
            A[j] = A[j - gap]
            j -= gap
        A[j] = key
    gap //= 2

print(A)