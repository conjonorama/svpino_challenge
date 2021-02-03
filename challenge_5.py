# Write a function that finds the largest and smallest number in an unsorted array.


# My attempt - using min & max variables and a loop
def minmax(arr):
    min = 0
    max = 0

    for i in arr:
        if i < min or min == 0:
            min = i
        if i > max:
            max = i

    return min, max

# My attempt 2 - using list min and max modules
def minmax2(arr):
    return min(arr), max(arr)
    

if __name__ == '__main__':
    import random
    t = []
    for i in range(20):
        t.append(random.randint(1,100))

    print(t)
    print(minmax(t))
    print(minmax2(t))