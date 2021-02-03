# Write a function that removes every duplicate value in an array.

# There could be more than one value duplicated. You should remove all of them leaving a single copy of the value.

# My attempt 1 - using list
def findUnique(arr):
    t = []
    for i in arr:
        if i not in t:
            t.append(i)
    return(t)

# My attempt 2 - using dictionary and taking keys out
def findUnique2(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1

    t = []
    for k in d.keys():
        t.append(k)

    return t
    # return d.keys()

# Twitter answer 1 - usings sets() --> Need to learn more about sets
def findUnique3(arr):
    return list(set(arr))

if __name__ == '__main__':
    array = 'a b b c d c d e f f g h'.split()
    print(findUnique(array))
    print(findUnique2(array))
    print(findUnique3(array))
