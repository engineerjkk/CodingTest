def str_to_minutes(time_str):
    """HH:MM 형식의 시간 문자열을 분으로 변환"""
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_str(minutes):
    """분을 HH:MM 형식의 시간 문자열로 변환"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def solution(n, t, m, timetable):
    # 크루들의 도착 시간을 분으로 변환하고 정렬
    crew_times = sorted([str_to_minutes(time) for time in timetable])
    
    # 첫 셔틀은 09:00 (540분)부터 시작
    start_time = 540
    
    # 마지막 셔틀 전까지는 크루를 태우고 지나감
    current_crew_idx = 0
    
    # 마지막 셔틀 전까지 각 셔틀 운행
    for bus in range(n-1):
        bus_time = start_time + (bus * t)
        # 현재 셔틀에 태울 수 있는 크루 수만큼 태움
        for _ in range(m):
            if current_crew_idx < len(crew_times) and crew_times[current_crew_idx] <= bus_time:
                current_crew_idx += 1
            else:
                break
    
    # 마지막 셔틀 시간
    last_bus = start_time + (n-1) * t
    
    # 마지막 셔틀에 탈 수 있는 크루 확인
    last_bus_crew = 0
    for i in range(current_crew_idx, len(crew_times)):
        if crew_times[i] <= last_bus:
            last_bus_crew += 1
            if last_bus_crew == m:  # 마지막 셔틀이 꽉 찰 경우
                return minutes_to_str(crew_times[i] - 1)
    
    # 마지막 셔틀에 자리가 남은 경우
    if last_bus_crew < m:
        return minutes_to_str(last_bus)
    # 마지막 셔틀에 자리가 없는 경우
    else:
        return minutes_to_str(crew_times[current_crew_idx + m - 1] - 1)
