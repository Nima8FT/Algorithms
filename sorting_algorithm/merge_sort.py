def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    B = merge_sort(arr[:mid])
    C = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            result.append(B[i])
            i += 1
        else:
            result.append(C[j])
            j += 1

    result.extend(B[i:] + C[j:])

    return result

A = [38, 27, 3, 43, 5]
output = merge_sort(A)
print(output)
