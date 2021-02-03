# Write a function that finds the duplicate number in an unsorted array containing every number from 1 to 100
# Only one of the numbers will appear twice.

# My attempt - I will be using a dictionary to compile the occurences and then will take the top occuring number

def findDupe(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1

    t = []
    for k, v in d.items():
        t.append((v, k))

    t.sort(reverse = True)

    return(t[0][1])


# Answer from twitter - very smart
def findDupe2(arr):
    expt = (len(arr))*(len(arr) - 1)/2
    rslt = sum(arr)

    return rslt - expt


if __name__ == '__main__':
    t_test = [1,3,3,5,4,2,6,7,8,9]
    print(findDupe(t_test))
    print(findDupe2(t_test))