def solution(n):
    answer = 0
    s=[0,1,2]
    for i in range(3,n+1):
        a=s[-2]+s[-1]
        s.append(a%1000000007)
    return s[-1]