# Write a function that finds the missing number in an unsorted array containing
#  every one of the other 99 numbers ranging from 1 to 100

# My initial attempt using
def find_missing(arr):
    missing = 0
    for i in range(1,101):
        if i not in arr:
            missing = i
    return missing

# Creating a random array from 1 to 100 and removing 1 number from array
import random
t = []
for i in range(1, 101):
    t.append(i)

indexDeleted = random.randint(1, 100)
print(indexDeleted)

del t[indexDeleted-1]
print(t)

print(find_missing(t))

# Submission 1 from twitter (Which is so simple and funny)
# If it's always from 1 to 100 it's pretty simple - in Python 3:
# https://twitter.com/RomuloF27/status/1354060816908226565?s=20

def findMissingNumber(arr):
    return 5050 - sum(arr)

# Sumbmission2 from Twitter
# I have no idea what is going on in this code - getting there though :)
# https://twitter.com/shraddha_pooja/status/1354136657927270401?s=20
def findMissingNumber1(arr):
    arr_len = len(arr)
    n = arr_len + 1
    missing_num = (n>>1)&1 ^ (1 if ((n&1)>0) else n) #XOR 1 to n
    for _ in range(arr_len): missing_num ^= arr[_]
    return missing_num

print(findMissingNumber1([1,4,3,5,7,6,8,2,11,9]))