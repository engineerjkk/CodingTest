import heapq

def min_meeting_rooms(N, meetings):
    # 시작 시간과 종료 시간을 따로 저장
    start_times = []
    end_times = []
    
    # 시작 시간과 종료 시간을 분리하여 정렬
    for start, end in meetings:
        start_times.append(start)
        end_times.append(end)
    
    # 시작 시간과 종료 시간을 정렬
    start_times.sort()
    end_times.sort()
    
    rooms = 0  # 현재 사용 중인 회의실 수
    max_rooms = 0  # 필요한 최대 회의실 수
    s = 0  # 시작 시간 인덱스
    e = 0  # 종료 시간 인덱스
    
    # 모든 시작 시간과 종료 시간을 처리할 때까지 반복
    while s < N:
        if start_times[s] < end_times[e]:
            # 새로운 회의 시작
            rooms += 1
            s += 1
        elif start_times[s] > end_times[e]:
            # 회의 종료
            rooms -= 1
            e += 1
        else:
            # 동시에 시작하고 끝나는 경우
            s += 1
            e += 1
        
        # 최대 회의실 수 갱신
        max_rooms = max(max_rooms, rooms)
    
    return max_rooms

# 입력 받기
N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 결과 출력
print(min_meeting_rooms(N, meetings))