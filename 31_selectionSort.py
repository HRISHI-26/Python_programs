arr = [9, 4, 2, 1, 7]
n = len(arr)

for i in range(n-1):
    max_idx = i
    for j in range(i+1, n):
        if arr[max_idx] > arr[j]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
print(f"Array: {arr}")