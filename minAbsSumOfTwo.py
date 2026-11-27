def solution(A):
    A.sort()
    min = float('inf')
    for i in range(len(A)):
        for j in range(i, len(A)):
            if abs(A[i] + A[j]) < min:
                min = abs(A[i] + A[j])
    return min