# Write a function that finds a subarray whose sum is equal to a given value.

# My attempt 1 - using itertools
def subArrSum(arr, n, tot):
    import itertools
    combs = itertools.combinations(arr, n)
    t = []
    for i in combs:
        if sum(i) == tot:
            t.append(i)
    
    return t


if __name__ == '__main__':
    array = [2000, 20, 19, 1999, 25, 2005]
    print(subArrSum(array, 2, 2020))