def solution(picks, minerals):
    answer = 0
    sum=0
    for i in picks:
        sum+=i
    min_sum=sum*5
    if len(minerals)>min_sum:
        minerals=minerals[:min_sum]
    new_minerals=[[0,0,0] for _ in range(min_sum//5+1)]
    for m in range(len(minerals)):
        if minerals[m]=="diamond":
            new_minerals[m//5][0]+=1
        elif minerals[m]=="iron":
            new_minerals[m//5][1]+=1
        else:
            new_minerals[m//5][2]+=1
    new_minerals.sort(key=lambda x:[x[0],x[1],x[2]],reverse=True)
    for mineral in new_minerals:
        dia,iron,stone=mineral
        for i in range(len(picks)):
            if picks[i]>0 and i==0:
                picks[i]-=1
                answer+=dia+iron+stone
                break
            elif picks[i]>0 and i==1:
                picks[i]-=1
                answer+=dia*5+iron+stone
                break
            elif picks[i]>0 and i==2:
                picks[i]-=1
                answer+=dia*25+iron*5+stone
                break
    return answer