arr = [1, 2, 3, 4, 5]
key = 1

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == key:
        print(f"Element found at {mid}")
        break
    elif arr[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")
