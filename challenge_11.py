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


# Twitter answer 1
def min_dif(arr):
    min_index = 0
    for i in range(0, len(arr)):
        if abs(sum(arr[:i]) - sum(arr[i:])) < abs(sum(arr[:min_index]) - sum(arr[min_index:])):
            min_index = i
    return(arr[:min_index], arr[min_index:])

t = [1,2,3,4,5,6,7,8,9]

print(minDiffArr(t))
print(min_dif(t))
