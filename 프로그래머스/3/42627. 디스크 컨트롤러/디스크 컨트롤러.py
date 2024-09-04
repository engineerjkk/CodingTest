import heapq

def solution(jobs):
    jobs.sort()  # 작업을 시작 시간 기준으로 정렬
    total_time = 0
    current_time = 0
    job_count = len(jobs)
    pq = []
    job_index = 0

    while job_index < job_count or pq:
        # 현재 시간 이전에 요청된 모든 작업을 우선순위 큐에 추가
        while job_index < job_count and jobs[job_index][0] <= current_time:
            heapq.heappush(pq, (jobs[job_index][1], jobs[job_index][0]))  # (소요 시간, 시작 시간)
            job_index += 1

        if pq:
            # 가장 짧은 작업 실행
            duration, start_time = heapq.heappop(pq)
            current_time += duration
            total_time += current_time - start_time
        else:
            # 큐가 비어있다면 다음 작업의 시작 시간으로 이동
            current_time = jobs[job_index][0] if job_index < job_count else current_time + 1

    return total_time // job_count