arr = [20, 50, 30, 40, 10]
n = len(arr)

print(f"Actual array: {arr}")

# Ascending
for index_1 in range(n-1):
    max_index = index_1
    for index_2 in range(index_1 + 1, n):
        if arr[max_index] > arr[index_2]:
            max_index = index_2
    arr[index_1], arr[max_index] = arr[max_index], arr[index_1]

print(f"Ascending order: {arr}")

# Descending
for index_1 in range(n-1):
    min_index = index_1
    for index_2 in range(index_1 + 1, n):
        if arr[min_index] < arr[index_2]:
            min_index = index_2
    arr[index_1], arr[min_index] = arr[min_index], arr[index_1]

print(f"Descending order: {arr}")