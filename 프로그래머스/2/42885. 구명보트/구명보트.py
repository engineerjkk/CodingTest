def solution(people, limit):
    answer = 0
    people.sort()  # 사람들의 몸무게를 오름차순으로 정렬

    a = 0  # 가장 가벼운 사람을 가리키는 포인터
    b = len(people) - 1  # 가장 무거운 사람을 가리키는 포인터
    while a <= b:
        if people[a] + people[b] <= limit:
            # 가장 가벼운 사람(a)과 가장 무거운 사람(b)을 함께 보트에 태울 수 있는 경우
            a += 1  # 가벼운 사람을 다음 사람으로 이동
        # 무거운 사람은 항상 보트에 태움
        b -= 1  # 무거운 사람을 다음 무거운 사람으로 이동
        answer += 1  # 필요한 보트의 수 증가

    return answer  # 모든 사람을 구출하는 데 필요한 보트의 최솟값 반환

# 예시 테스트 케이스
print(solution([70, 50, 80, 50], 100))  # 출력: 3
print(solution([70, 80, 50], 100))  # 출력: 3
