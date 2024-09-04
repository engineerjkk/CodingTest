def solution(n):
    answer = 0
    s=[0,1]
    for i in range(2,n+1):
        a=s[-1]+s[-2]
        s.append(a%1234567)
    return s[-1]