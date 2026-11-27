def solution(A):
    A.sort()
    # 0 < P < Q < R < N
    # P + Q > R
    # Q + R > P already true
    # R + P > Q
    # dumb solution would be O(n^3) so cannot be that
    # solution has to use less loops
    # if all three equal, true
    # A[p] + A[q] > A[r] and q = r+1
    # if P + Q > R is false, trying to increase q would not be needed
    # e.g. 1, 2, 6, 9, 10
    # same logic applies to R + P > Q
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2] and A[i+2] + A[i] > A[i+1]:
            return 1
    return 0