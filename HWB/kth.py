# A.J. Imholte
# Algorithm Design and Analysis
# HWB


"""
A recursive function returns a subset of a given list based off a given parameter k which is greater than or equal to
one.
"""
def kth(L,k):
    if len(L) < k: # base case: if the length of the list is less than the value of k, return an empty list
        return []
    else:
        # recursive case
        element = [L[k -  1]] # the element that we want to return from the list
        return element + kth(L[k:],k) # return the element plus the output from the recursive case of kth(L[k:], k)
    # this works in this example because we are making the problem size smaller by slicing the list L by k things from
    # the front of the list
    pass


# A few test cases

lst1 = [3, 4, 1, 3]
for i in range(1,6):
    print(kth(lst1, i))

lst2 = ["Computer", "Science", "is", "fun", "especially", "recursion!", "Let's", "keep", "learning", "more!"]
for i in range(1, 12):
    print(kth(lst2, i))