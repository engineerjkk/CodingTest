def solution(n, s):
    
    if n>s:
        return [-1]
    answer=[]
    for _ in range(n):
        answer.append(s//n)
    
    for i in range(s%n):
        answer[i]+=1
    answer.sort()

    return answer