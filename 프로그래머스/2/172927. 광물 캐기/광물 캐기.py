def solution(picks, minerals):
    answer = 0
    
    # 곡괭이 수
    sum = 0
    for p in picks:
        sum += p
        
    # 곡괭이로 캘 수 있는 만큼 광물 자르기
    min_num = sum * 5       
    if len(minerals) > min_num:
        minerals = minerals[:min_num]
        
    # 광물 5개씩 묶어서 정렬 (다이아, 철, 돌 순서대로)
    new_minerals = [[0, 0, 0] for _ in range(len(minerals)//5 + 1)]
    for m in range(len(minerals)):
        if minerals[m] == 'diamond':
            new_minerals[m//5][0] += 1
        elif minerals[m] == 'iron':
            new_minerals[m//5][1] += 1
        else:
            new_minerals[m//5][2] += 1
    
    new_minerals.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)
    
    # 피로도 계산
    for i in new_minerals:
        dia, iron, stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += dia * 5 + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1 
                answer += dia * 25 + iron * 5 + stone
                break    
    
    return answer