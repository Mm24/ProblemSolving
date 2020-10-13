"""

Problem Overview

Given an array of size N, find the number of swaps/shifts of elements which will be done as the array is sorted using insertion sort.


Insertion sort

The most obvious way will be to do an insertion sort and record the number of shifts required to sort it.
It will take O(N^2) time which means in the worst case under our constraints 5*10^10. We need to do better.
The obvious answer can be as large as 10^10 so we cannot count each shift one by one.
It gives us an idea that we need to shift elements in the same way as insertion
sort does, but not one position at a time. There is an algorithm which does just that.

Merge Sort

If you know merge sort you must have noticed that when we merge 2 sorted arrays if the element of the 2nd array(on the right)
is smaller we put its element in the new sorted array which indirectly means we are shifting that element to the left by
the number of elements remaining in the 1st array. We are actually shifting the element but in a higher order.
That is why merge sort's complexity is O(N logN), which is the complexity of this problem.
We just need to implement merge sort and add the shifts when an element of the 2nd array is less then the element of 1st array.


"""

def inversions(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = n/2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 <n1 and (i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans


def insertionSort(array):
    mid = len(array) // 2
    # Sorting mid left
    left_swaps, left_sorted = insertionSort(array[:mid])
    # Sorting mid right
    right_swaps, right_sorted = insertionSort(array[mid:])

    merge_swaps = 0
    arr_sort = []
    while left_sorted and right_sorted:
        if left_sorted[0] <= right_sorted[0]:
            arr_sort.append(left_sorted.pop(0))
        else:
            arr_sort.append(right_sorted.pop(0))
            merge_swaps += len(left_sorted)

    # merge the list
    arr_sort.extend(left_sorted)
    arr_sort.extend(right_sorted)
    swaps = left_swaps + right_swaps + merge_swaps
    return swaps, arr_sort


if __name__ == '__main__':
    for _ in range(input()):
        n = input()
        arr = map(int,  input().split())
        counts = inversions(arr)
        print(counts)


def insertionSort(arr):
    length = len(arr)
    if (length <= 1):
        return arr, 0

    # Middle Sort
    mid = length // 2
    left_arr,  n_lswaps = insertionSort(arr[0:mid])
    right_arr, n_rswaps = insertionSort(arr[mid:length])
    swaps = n_lswaps + n_rswaps

    index_right = 0
    len_right = len(right_arr)
    index_left = 0
    len_left = len(left_arr)

    # Merge
    merged_arr = []
    while index_left < len_left:
        if index_right < len_right and left_arr[index_left] > right_arr[index_right]:
            merged_arr.append(right_arr[index_right])
            index_right += 1
            swaps += len_left - index_left
        else:
            merged_arr.append(left_arr[index_left])
            index_left += 1

    merged_arr[len_left + index_right:] = right_arr[index_right:]
    return merged_arr, swaps