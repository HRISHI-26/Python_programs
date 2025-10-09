arr = [10, 40, 20, 30, 50]
n = len(arr)

print(f"Actual array: {arr}")
# Ascending
for index_1 in range(n-1):
    for index_2 in range(index_1 + 1, n):
        if arr[index_1] > arr[index_2]:
            arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
    
print(f"Ascending order: {arr}")

# Descending 
for index_1 in range(n-1):
    for index_2 in range(index_1 + 1, n):
        if arr[index_1] < arr[index_2]:
            arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

print(f"Descending order: {arr}")
