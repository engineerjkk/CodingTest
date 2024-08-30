def solution(A, B):
    answer=0
    cnt=0
    A.sort()
    B.sort()
    for i in range(len(A)):
        if A[cnt]<B[i]:
            cnt+=1
            answer+=1
    return answer