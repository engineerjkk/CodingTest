import sys
def solution(n):
    answer = ""
    lst=[]
    sol=sys.maxsize
    while n>0:
        n, res =divmod(n,3)
        answer+=str(res)
        
    return int(answer,3)