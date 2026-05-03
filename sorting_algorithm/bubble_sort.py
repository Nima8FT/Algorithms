A = [16, 5, 8, 1, 10, 9, 7, 25, 57, 64, 23, 1, 9, 87]

n = len(A)

for i in range(n):
    swapped = False

    for i in range(n - 1, 0, -1):
        if A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]
            swapped = True
        
    if not swapped:
        break;

print(A)