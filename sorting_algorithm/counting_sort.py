A = [2, 1, 3, 4, 5, 3, 5, 1, 2]

max_val = max(A)
arr = [0] * (max_val + 1)

for i in A:
    arr[i] += 1

out_list = []
for i in range(max_val + 1):
    out_list += [i] * arr[i]

print(out_list)