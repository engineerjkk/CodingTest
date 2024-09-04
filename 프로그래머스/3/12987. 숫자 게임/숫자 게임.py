def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        if B[i]>A[answer]:
            answer+=1
    return answer