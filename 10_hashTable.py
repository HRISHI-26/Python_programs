arr = [23, 34, 32, 15, 53]
hash = {}

for i, num in enumerate(arr):
    if num not in hash:
        hash[i + 1] = num

print(hash)
