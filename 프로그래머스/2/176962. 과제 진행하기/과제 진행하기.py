def solution(plans):
    # 1. 시작 시간을 분(minute) 단위로 변환
    converted_plans = []
    for plan in plans:
        name = plan[0]  # 과제 이름
        start_time = plan[1]  # 시작 시각
        playtime = int(plan[2])  # 소요 시간

        # 시작 시각을 분 단위로 변환
        hours, minutes = map(int, start_time.split(':'))
        start_time_in_minutes = hours * 60 + minutes

        # 변환된 데이터를 리스트에 추가
        converted_plans.append([name, start_time_in_minutes, playtime])

    # 2. 시작 시간을 기준으로 내림차순 정렬
    converted_plans.sort(key=lambda x: -x[1])
    
    lst = []  # 완료된 과제들을 기록할 리스트
    while converted_plans:
        x = converted_plans.pop()  # 가장 늦게 시작하는 과제를 하나씩 꺼냅니다.
        for i, v in enumerate(lst):
            if v[0] > x[1]:
                lst[i][0] += x[2]  # 새로운 과제 시작 시점이 이전 과제가 끝난 시점보다 빠르면 시간을 연장합니다.
        lst.append([x[1] + x[2], x[0]])  # 과제를 끝낸 시간을 저장합니다.
    lst.sort()  # 과제들을 완료한 시각 순으로 정렬합니다.

    return list(map(lambda x: x[1], lst))  # 과제 이름만 추출해서 반환합니다.
