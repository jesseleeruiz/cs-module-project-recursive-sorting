# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = arrA + arrB

    # Your code here
    some_num1 = some_num2 = some_num3 = 0

    while some_num1 < len(arrA) and some_num2 < len(arrB):
        if arrA[some_num1] <= arrB[some_num2]:
            merged_arr[some_num3] = arrA[some_num1]
            some_num1 += 1
        else:
            merged_arr[some_num3] = arrB[some_num2]
            some_num2 += 1
        some_num3 += 1

    while some_num1 < len(arrA):
        merged_arr[some_num3] = arrA[some_num1]
        some_num1 += 1
        some_num3 += 1

    while some_num2 < len(arrB):
        merged_arr[some_num3] = arrB[some_num2]
        some_num2 += 1
        some_num3 += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        if len(left) > 1:
            left = merge_sort(left)
        if len(right) > 1:
            right = merge_sort(right)

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     pass
    # Your code here


# def merge_sort_in_place(arr, l, r):
#     pass
    # Your code here

