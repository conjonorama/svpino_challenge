# Write a function that finds the contiguous subarray of a given size with the largest sum.

# My attempt 1 - using a for loop and list slicing
def maxSub(arr, n):
    maxArr = sum(arr[:n])
    
    for i in arr[0:]:
        if sum(arr[i:i+n]) > maxArr:
            maxArr = sum(arr[i:i+n])

    return maxArr

if __name__ == '__main__':
    t = [1,2,3,4,5,6,7,8]
    print(maxSub(t, 3))