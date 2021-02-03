# Write a function that, given an array, determines if you can partition it in two separate subarrays such that the sum of elements in both subarrays is the same.

# My attempt 1 - using itertools
def splitSum(arr):
    import itertools
    combs = itertools.combinations(arr,int(len(arr)/2))
    for i in combs:
        print(i)

# Twitter example - very clever, can't really beat it at this moment.
def equal_sums(arr):
    idx = 0
    while idx < len(arr):
        if sum(arr[:idx]) == sum(arr[idx:]):
            return arr[idx:], arr[:idx]
        idx += 1

t1 = [2,2,3,3,4,6]
print(equal_sums(t1))
# splitSum(t1)