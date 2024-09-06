def solution(picks, minerals):
    answer = 0
    total_picks=0
    for i in picks:
        total_picks+=i
    total_picks*=5
    if total_picks<len(minerals):
        minerals=minerals[:total_picks]
    new_minerals=[[0,0,0] for _ in range(total_picks//5+1)]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        else:
            new_minerals[i//5][2]+=1
    new_minerals.sort(key=lambda x:[x[0],x[1],x[2]],reverse=True)
    for mineral in new_minerals:
        dia,iron,stone=mineral
        for i in range(3):
            if i==0 and picks[i]>0:
                picks[i]-=1
                answer+=dia+iron+stone
                break
            if i==1 and picks[i]>0:
                picks[i]-=1
                answer+=dia*5+iron+stone
                break
            if i==2 and picks[i]>0:
                picks[i]-=1
                answer+=dia*25+iron*5+stone
                
    return answer