def solution(n):
    i=0
    for i in range(0,int(n**(0.5))+1):
        if i**2==n:
            return (i+1)**2
    return -1