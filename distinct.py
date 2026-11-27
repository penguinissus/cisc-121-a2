# returns number of distinct elements in the list
def solution(A):
    #set(A) gives the list with only its own distinct elements
    #len() gives the number of elements in that list
    return len(set(A))