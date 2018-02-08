
# given a list and an integer k,
# return a list where the elements are L[k-1, 2k-1, 3k-1...n-1*k-1]

# if the length of the list is less than or equal to the value of k
    # return an empty list

# else
    # add the element at L[k-1] to a list (this will be returned)
    # delete from the list in range of k
    # call the function again on the new list with the same k

# Keep track of what index we are at (set this equal to 1 at first)
# If the index is greater than or equal to the length of list
    # Stop and return the new list
# Else
    # add the element L[index * k - 1] to the sublist
    # add this sublist to the solution list
    # increment index
    # call kth(index*k - 1)
    # retun the list

def kth(L,k):
    if len(L) <= k:
        return []
    else:
        element = [L[k -  1]]
        return kthList + kth(L[:-1], k)
    pass

print(kth([3, 4, 1, 3], 1))