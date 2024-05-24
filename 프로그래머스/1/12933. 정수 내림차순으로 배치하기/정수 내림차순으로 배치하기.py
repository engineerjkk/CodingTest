def solution(n):
    a=list(map(int,str(n)))
    a.sort(reverse=True)
    b=""
    for i in a:
        b+=str(i)
    answer=int(b)
    return answer