A = [29, 10, 14, 37, 18]

n = len(A)
gap = n
is_sorted = False

while not is_sorted:
    gap = int(gap / 1.3)
    if gap <= 1:
        gap = 1
        is_sorted = True

    i = 0
    while i + gap < n:
        if A[i] > A[i + gap]:
            A[i], A[i + gap] = A[i + gap], A[i]
            is_sorted = False
        i += 1

print(A)