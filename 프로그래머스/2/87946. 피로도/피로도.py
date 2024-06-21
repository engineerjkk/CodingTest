from itertools import permutations
def solution(k, dungeons):
    n=len(dungeons)
    lst=[]
    for i in range(n):
        lst.append(i)
    nCr=permutations(lst,n)
    result=0
    for x in nCr:
        k2=k
        flag=True
        time=0
        for i in x:       
            minimum_HP=dungeons[i][0]
            need_HP=dungeons[i][1]
            if k2<minimum_HP:
                continue
            k2-=need_HP
            time+=1
        result=max(result,time)        
    return result