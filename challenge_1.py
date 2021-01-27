# Write a function that reverses an array in place.
# In other words, the function should not use and auxilary array to do the work.

def reverseArray(arr):
    '''
    Take input arr, and reverses it.
    '''
    t = []
    while len(arr) > 0:
        t.append(arr[-1])
        arr = arr[:-1]
    return t

# arr = ['BMW', 'Ford', 'Audi', 'GMC', 'Subaru', 'Honda', 'Tesla'] # Test data
# print(reverseArray(arr)) # Success

# Here are some other interesting ones from the same twitter thread

# 1 - Using the list method 'reverse'
def reverseArray1(arr):
    arr.reverse() # Reverses list in place
    return arr

# print(reverseArray1(arr)) # Success

# 2 - Using multiple assignment and splitting the list in half
import math
def reverseArray2(arr):
    arr_len = len(arr) # Length of list
    for i in range(math.ceil(arr_len/2)): # Rounds list length divided by 2 up to nearest whole number
        arr[i], arr[arr_len-i-1] = arr[arr_len-i-1], arr[i] # Multiple assignemnt - assigns first to last and last to first
    return arr

# print(reverseArray2(arr)) # Success

