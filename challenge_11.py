# Write a function that, given an array, divides it into two subarrays, such as the absolute difference between their sums is minimum.


# My attempt 1 - assuming we can split anywhere in the array and that each number stays where it is within the array.
def minDiffArr(arr):
    diff_arr = max(arr)
    idx = 0
    for i in range(len(arr)):
        arr1 = arr[:i]
        arr2 = arr[i:]
        diff = abs(sum(arr1)-sum(arr2))
        if diff < diff_arr:
            diff_arr = diff
            idx = i
    return diff_arr, idx

t = [1,2,3,4,5,6]

print(minDiffArr(t))
