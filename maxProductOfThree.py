def solution(A):
    # max function returns the largest value in the list
    # remove that number then repeat to find the next largest number
    max1 = max(A)
    A.remove(max1)
    max2 = max(A)
    A.remove(max2)
    max3 = max(A)
    return max1*max2*max3