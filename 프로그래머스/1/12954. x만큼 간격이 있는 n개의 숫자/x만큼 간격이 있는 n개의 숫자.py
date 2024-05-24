def solution(x, n):
    answer=[]
    ans=0
    for _ in range(n):
        ans+=x
        answer.append(ans)
    return answer