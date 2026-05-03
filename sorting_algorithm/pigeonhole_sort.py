A = [2, 1, 3, 4, 5, 3, 5, 1, 2]

min_val = min(A)
max_val = max(A)
range_val = max_val - min_val + 1

holes = [[] for i in range(range_val)]

for num in A:
    holes[num - min_val].append(num)

result = []
for hole in holes:
    result.extend(hole)

print(result)