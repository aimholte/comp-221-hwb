# A.J. Imholte
# Algorithm Design and Analysis
# HWB

import math

"""
A simple function used to determine if two lists contain any identical values.
"""
def disjoint(A, B): # A and B are lists
    for i in range(len(A)): # iterate over the first list
        for j in range(len(B)): # iterate over the second list
            if A[i] == B[j]:
                return False # returns false if a given value is in both lists
    return True # returns true if the two lists share no common values


# Test Cases
print(disjoint([3,2,5], [1,4,6])) # expected output: true
print(disjoint([3,2,5], [1,2,3])) # expected output: false
print(disjoint([-2,-1,0], [1,2]))  # expected output: true
print(disjoint([1], [2,6,8,3,1]))  # expected output: false
print(disjoint([], [5,4]))  # expected output: true
print(disjoint([], []))  # expected output: true
print(disjoint([1,33,44,5], [10, 11, 12, 44]))  # expected output: false
print(disjoint([10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3]))  # expected output: true
print(disjoint([-1], [1]))  # expected output: true
print(disjoint([-12.5, 12.5], [-12.5, 10.5]))  # expected output: false
print(disjoint([0, 0, 0], [0.0001, 0.0])) # expected output: false
print(disjoint([0.0000005, 1.5], [0.0000005, 1.25])) # expected output: false
print(disjoint([1, 1, 1.11, 91], [19, 0, 10, 1.12])) # expected output: true
print(disjoint([math.cos(100), math.exp(2)], [math.exp(10), 100.0, math.sin(90), math.cos(100)])) # expected output: false
print(disjoint([1/2, 1/4, 1/5], [3/4, 2/5, 1/2])) # expected output: false
print(disjoint(["more", "programming", "here"], ["here", "is", "some", "more"])) # expected output: false
print(disjoint(["starting", "to run out of", "ideas"], ["please", "help"])) # expected output: true
print(disjoint([math.inf+100], [math.inf+1])) # Example of where inputs break the code...
