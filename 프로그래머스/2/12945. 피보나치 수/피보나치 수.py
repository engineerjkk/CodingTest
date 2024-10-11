def solution(n):
    s=[0,1]
    for i in range(2,n+1):
        c=s[i-1]+s[i-2]
        s.append(c%1234567)
    return s[-1]