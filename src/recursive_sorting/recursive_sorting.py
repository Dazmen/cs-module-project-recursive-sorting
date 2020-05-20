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
    left_end = mid
    right_start = mid +1

    while start <= left_end and right_start <= end:
        if arr[start] <= arr[right_start]:
            start += 1
        else:
            # swap values
            index = right_start
            while index != start:
                arr[index - 1], arr[index] = arr[index], arr[index - 1]
                index -= 1
            # value is now moved to the front
            # update pointers
            start += 1
            left_end += 1
            right_start += 1
    #  values are being overwritten
    return arr


def merge_sort_in_place(arr, left, right):
    # Your code here

    if left < right:
        mid = (left + right) // 2
        merge_sort_in_place(arr, left, mid)
        merge_sort_in_place(arr, mid + 1, right)

        merge_in_place(arr, left, mid, right)

    return arr 


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
