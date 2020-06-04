def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #with binary, we're cutting the array in half each time, we need to define these halves
    low = 0
    #high will never go beyond the length of the array
    high = len(arr) - 1
    mid = 0

    while low <= high:

        #set the middle
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid


    return -1  # not found
