def solution(A):
    A.sort()
    if A[-1]*A[-2]*A[-3] > A[0]*A[1]*A[-1]:
        return A[-1]*A[-2]*A[-3]
    else: 
        return A[0]*A[1]*A[-1]