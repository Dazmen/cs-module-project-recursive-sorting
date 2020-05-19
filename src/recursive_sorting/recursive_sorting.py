# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left_arr, right_arr):
    # elements = len(left_arr) + len(right_arr)
    # merged_arr = [0] * elements

    # Your code here
    merged_array = []
    left_pointer = 0
    right_pointer = 0
    
    while left_pointer < len(left_arr) and right_pointer < len(right_arr):
        if left_arr[left_pointer] > right_arr[right_pointer]:
            merged_array.append(right_arr[right_pointer])
            right_pointer += 1
        else:
            merged_array.append(left_arr[left_pointer])
            left_pointer += 1

    merged_array.extend(left_arr[left_pointer:])
    merged_array.extend(right_arr[right_pointer:])

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    split_point = len(arr) // 2

    if split_point < 1:
        return arr

    left_arr = arr[:split_point]
    right_arr = arr[split_point:]


    return merge(merge_sort(left_arr), merge_sort(right_arr))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
