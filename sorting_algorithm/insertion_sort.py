A = [16, 5, 8, 1, 10, 9, 7, 25, 57, 64, 23, 1, 9, 87]

n = len(A)

for i in range(1, n):
    key = A[i]
    j = i - 1

    while j >= 0 and key < A[j]:
        A[j + 1] = A[j]
        j -= 1
 
    A[j + 1] = key

print(A)