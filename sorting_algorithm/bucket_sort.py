A = [12, 8, 37, 28, 98, 42, 55, 82, 10, 67, 24, 72, 2, 31, 49, 50, 78, 86, 92]

n = len(A)

num_buckets = 10
buckets = [[] for i in range(num_buckets)]

for num in A:
    index = num // 10
    buckets[index].append(num)

for i in range(num_buckets):
    buckets[i] = sorted(buckets[i])

result = []
for bucket in buckets:
    result.extend(bucket)

print(result)