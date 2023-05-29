def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Target found at index mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in the right half


# Example usage:
arr = [2, 12, 23, 45, 67, 89]
target = 23
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print("Target found at index" ,result)
else:
    print("Target not found")
