def solution(n):
    s=[0,1]
    a=1
    for i in range(2,n+2):
        a=s[-2]+s[-1]
        s.append(a)
    return s[-1]%1234567