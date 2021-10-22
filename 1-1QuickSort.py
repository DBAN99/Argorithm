def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    less_arr, same_arr, more_arr = [], [], []

    for num in arr:
        if num < pivot:
            less_arr.append(num)

        elif num > pivot:
            more_arr.append(num)

        else:
            same_arr.append(num)

    return quick_sort(less_arr) + same_arr + quick_sort(more_arr)

arr = [4,6,9,8,7,5,3,2,1]
print(quick_sort(arr))