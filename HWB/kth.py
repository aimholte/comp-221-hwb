
# given a list and an integer k,
# return a list where the elements are L[k-1, 2k-1, 3k-1...n-1*k-1]

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
    kthList = []
    if len(L) <= 0:
        return 0
    else:
        element = L[len(L) * k - 1]
        kthList.append(element)
        return kthList + kth(L[:-1], k)
    pass

print(kth([3, 4, 1, 3], 1))