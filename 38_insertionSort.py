arr = [10, 50, 30, 20, 40]
n = len(arr)

# Ascending 
for index_1 in range(n):
    key = arr[index_1]
    index_2 = index_1 - 1
    while index_2 >= 0 and key < arr[index_2]:
        arr[index_2 + 1] = arr[index_2]
        index_2 -= 1
    arr[index_2 + 1] = key

print(f"Ascending order: {arr}")

# Descending
for index_1 in range(n):
    key = arr[index_1]
    index_2 = index_1 - 1
    while index_2 >= 0 and key > arr[index_2]:
        arr[index_2 + 1] = arr[index_2]
        index_2 -= 1
    arr[index_2 + 1] = key

print(f"Descending order: {arr}")
        