def solution(A, B):
    A.sort()
    B.sort()
    answer=0
    cnt=0
    for i in range(len(A)):
        if B[i]>A[cnt]:
            answer+=1
            cnt+=1
    return answer