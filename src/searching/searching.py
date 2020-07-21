# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid)
    else:
        return mid
    # Your code here


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     pass
    # Your code here

