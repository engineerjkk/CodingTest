def solution(n,a,b):
    a=a-1
    b=b-1
    lst=[0]*n
    lst[a]=1
    lst[b]=1
    
    answer=0
    while n>=2:
        tmp=[]
        i=0
        while i<n-1:
            if lst[i]==0 and lst[i+1]==0:
                tmp.append(0)
            elif lst[i]==0 and lst[i+1]==1:
                tmp.append(1)
            elif lst[i]==1 and lst[i+1]==0:
                tmp.append(1)
            else:
                return answer+1
            i+=2
        answer+=1
        lst=tmp
        n=len(tmp)
            
            
        