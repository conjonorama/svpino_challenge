# Write a function that, given two arrays, finds the longest common subarray present in both of them.

# My attempt - triple for loops baby 
def lcsa(arr1, arr2):
    longestArr = []
    arr1_groups = []
    arr2_groups = []
    
    for i in range(len(arr1)+1):
        for j in range(len(arr1)+1):
            if arr1[i:j]:
                arr1_groups.append(arr1[i:j])
                
    for i in range(len(arr2)+1):
        for j in range(len(arr2)+1):
            if arr2[i:j]:
                arr2_groups.append(arr2[i:j])

    for i in arr1_groups:
        if i in arr2_groups and len(i) > len(longestArr):
            longestArr = i
    # print(arr1_groups)
    # print(arr2_groups)
    return longestArr

# Twitter response - not sure I copied this over right
    # def common_subarr(arr1, arr2):

    #     s1 = "".join(arr1)
    #     s2 = "".join(arr2)

    #     i = 0
    #     j = len(s1)

    #     for (sum(range(len(s1)))):
    #         tmp = s1.substring(i,j)
    #         if tmp in s2:
    #             return tmp.split()
    #         j -= 1
    #         if j < i:
    #             j = len(s1)
    #             i += 1

if __name__ == '__main__':
    t1 = [1, 1, 1, 3, 5, 6, 8]
    t2 = [1, 1, 3, 4, 5, 6, 8]

    print(lcsa(t1, t2))
    # print(common_subarr(t1, t2))