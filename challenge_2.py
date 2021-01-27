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


