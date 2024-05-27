def solution(n, m, section):
    lst=[1]*(n+1)
    for i in section:
        lst[i]=0
    answer=0
    for i in range(1,len(lst)):
        if i>(len(lst)-m):
            if lst[i]==0:
                answer+=1
                for j in range(i,len(lst)):
                    lst[j]=1
        else:
            if lst[i]==0:
                answer+=1
                for j in range(i,i+m):
                    lst[j]=1
    return answer