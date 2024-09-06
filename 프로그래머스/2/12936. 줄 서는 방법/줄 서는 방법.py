import math
def solution(n, k):
    answer = []
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    k-=1
    while lst:
        a=k//math.factorial(n-1)
        answer.append(lst[a])
        del lst[a]
        k=k%math.factorial(n-1)
        n-=1
        
    return answer