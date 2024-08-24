def solution(picks, minerals):
    answer = 0
    tmp=0
    for i in picks:
        tmp+=i
    min_minerals=tmp*5
    if min_minerals<len(minerals):
        minerals=minerals[:min_minerals]
    
    new_minerals=[[0,0,0] for _ in range(min_minerals//5+1)]
    for m in range(len(minerals)):
        if minerals[m]=='diamond':
            new_minerals[m//5][0]+=1
        elif minerals[m]=='iron':
            new_minerals[m//5][1]+=1
        else:
            new_minerals[m//5][2]+=1
    new_minerals.sort(key=lambda x:[x[0],x[1],x[2]],reverse=True)
    print(new_minerals)
    
    for m in new_minerals:
        dia,iron,stone=m
        for i in range(len(picks)):
            if picks[i]>0 and i==0:
                answer+=dia+iron+stone
                picks[i]-=1
                break
            elif picks[i]>0 and i==1:
                answer+=dia*5+iron+stone
                picks[i]-=1
                break
            elif picks[i]>0 and i==2:
                answer+=dia*25+iron*5+stone
                picks[i]-=1
                break
    return answer