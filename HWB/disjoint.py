# A.J. Imholte
# Algorithm Design and Analysis
# HWB

def disjoint(A, B): # A and B are lists
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return False
    return True

print(disjoint([3,2,5], [1,4,6]))
print(disjoint([3,2,5], [1,2,3]))
print(disjoint([-2,-1,0], [1,2]))
print(disjoint([1], [2,6,8,3,1]))
print(disjoint([], [5,4]))
print(disjoint([], []))
