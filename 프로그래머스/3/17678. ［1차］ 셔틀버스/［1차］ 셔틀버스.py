def solution(n, t, m, timetable):
    # 시간을 분으로 변환하는 함수
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes
    
    # 분을 시간 문자열로 변환하는 함수
    def minutes_to_time(minutes):
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"
    
    # 크루들의 도착 시간을 분으로 변환하고 정렬
    crew_times = sorted(map(time_to_minutes, timetable))
    
    # 셔틀버스 운행 시간 계산 (09:00부터 t분 간격으로 n회)
    bus_times = [9 * 60 + t * i for i in range(n)]
    
    # 마지막 버스 전까지 탑승 처리
    crew_idx = 0
    for i in range(n - 1):
        bus_time = bus_times[i]
        count = 0
        
        # 현재 버스에 크루 탑승 처리
        while count < m and crew_idx < len(crew_times) and crew_times[crew_idx] <= bus_time:
            crew_idx += 1
            count += 1
    
    # 마지막 버스에 대한 처리
    last_bus_time = bus_times[-1]
    last_crew_time = last_bus_time
    
    # 마지막 버스에 탈 수 있는 크루 수 계산
    last_bus_crews = []
    while crew_idx < len(crew_times) and crew_times[crew_idx] <= last_bus_time:
        last_bus_crews.append(crew_times[crew_idx])
        crew_idx += 1
    
    # 마지막 버스가 만석이 되는 경우
    if len(last_bus_crews) >= m:
        last_crew_time = last_bus_crews[m - 1] - 1
    else:
        last_crew_time = last_bus_time
    
    return minutes_to_time(last_crew_time)
