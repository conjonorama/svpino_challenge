# Write a function that, given two arrays, finds the length of the shortest array that contains both input arrays as subarrays.

# My first attempt - using a lot of same logic as in challenge 8
def shortCombo(arr1, arr2):
    from challenge_8 import lcsa
    longest_sub = lcsa(arr1, arr2)
    for i in longest_sub:
        if i in arr1:
            arr1.remove(i)
            arr2.remove(i)
    longest_sub = longest_sub + arr1 + arr2 # Need to figure out the augmented assignment operation here w/ two combos
    return(len(longest_sub), longest_sub)

t1 = [1, 1, 1, 3, 5, 6, 8]
t2 = [1, 1, 3, 4, 5, 6, 8]

print(shortCombo(t1, t2))