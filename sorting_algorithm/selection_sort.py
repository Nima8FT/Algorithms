A = [16, 5, 8, 1, 10, 9, 7, 25, 57, 64, 23, 1, 9, 87]

n = len(A)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if A[j] < A[min_idx]:
            min_idx = j
    if min_idx != i:
        A[i], A[min_idx] = A[min_idx], A[i]

print(A)
