def solution(A, K):
    # write your code in Python 3.6
    if len(A) == K or A.count(A[0]) == len(A):
        return A
    else:
        new_A = [0] * len(A)
        for i in range(0,len(A)):
            new_A[(i+(K % len(A)))%len(A)] = A[i]
        return new_A  