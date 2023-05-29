def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return x
    return -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_array = [2,3,5,7,9]
target = 112
result = binary_search(sorted_array, target)
if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the array.")
