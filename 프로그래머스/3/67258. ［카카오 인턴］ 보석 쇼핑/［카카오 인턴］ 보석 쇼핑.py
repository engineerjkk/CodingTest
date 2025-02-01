def solution(gems):
    # 전체 보석 종류 수
    n_gems = len(set(gems))
    
    # 보석 개수를 저장할 딕셔너리
    gem_count = {}
    

    answer = [1, len(gems), len(gems)]
    
    # 투 포인터 초기화
    start = 0
    end = 0
    
    while end < len(gems):
        # end 포인터 위치의 보석 추가
        if gems[end] not in gem_count:
            gem_count[gems[end]] = 1
        else:
            gem_count[gems[end]] += 1
            
        # 모든 종류의 보석을 포함하게 되면
        while len(gem_count) == n_gems:
            # 현재 구간이 더 짧으면 정답 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1, end - start]
                
            # start 포인터 위치의 보석 제거
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1
            
        end += 1
    
    return [answer[0], answer[1]]