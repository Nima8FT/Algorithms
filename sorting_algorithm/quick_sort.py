def quick_sort(arr):
    if len(arr) < 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


A = [12, 92, 35, 8, 46, 27]
print(quick_sort(A))
