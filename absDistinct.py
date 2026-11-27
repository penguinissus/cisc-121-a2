# uses similar logic compared to distinct problem, but we first need to make every value positive
def solution(A):
    for i in range(len(A)):
        # added early break so we don't need to loop through positive numbers
        if A[i] > 0:
            break
        A[i] = abs(A[i])
    return len(set(A))