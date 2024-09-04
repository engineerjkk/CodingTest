def solution(n, s):
    answer = []
    if s<n:
        return [-1]
    for _ in range(n):
        answer.append(s//n)
    for i in range(s%n):
        answer[i]+=1
    answer.sort()
    return answer