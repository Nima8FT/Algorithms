def heapify(arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

A = [4, 10, 3, 5, 1]

n = len(A)

for i in range(n // 2 - 1, -1, -1):
    heapify(A, n, i)

for i in range(n - 1, 0, -1):
    A[i], A[0] = A[0], A[i]
    heapify(A, i, 0)

print(A)
    