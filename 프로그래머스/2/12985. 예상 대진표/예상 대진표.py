def solution(n,a,b):
    a=a-1
    b=b-1
    lst=[0]*n
    lst[a]=1
    lst[b]=1
    ans=0
    while len(lst)>=2:
        i=0
        tmp=[]
        while i<n-1:
            if lst[i]==0 and lst[i+1]==0:
                tmp.append(0)
            elif lst[i]==0 and lst[i+1]==1:
                tmp.append(1)
            elif lst[i]==1 and lst[i+1]==0:
                tmp.append(1)
            elif lst[i]==1 and lst[i+1]==1:
                return ans+1
            i+=2
        lst=tmp
        n=len(tmp)
        #a,b=tmp.index(1)
        a,b=list(filter(lambda x: tmp[x] == 1, range(len(tmp))))
        ans+=1