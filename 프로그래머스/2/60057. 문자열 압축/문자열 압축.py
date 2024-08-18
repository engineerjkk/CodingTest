def solution(s):
    # 초기 답은 문자열 전체 길이
    answer = len(s)

    # 문자열을 자를 단위 길이 i를 1부터 len(s)//2까지 시도
    for i in range(1, len(s) // 2 + 1):
        compressed = ""  # 압축된 문자열을 저장할 변수
        prev = s[:i]  # 첫 번째 부분 문자열
        count = 1  # 반복 횟수 카운트

        # 단위 길이 i로 문자열을 순회하며 압축 시도
        for j in range(i, len(s), i):
            # 현재 부분 문자열 추출
            current = s[j:j + i]
            if prev == current:
                count += 1  # 이전 문자열과 같으면 카운트 증가
            else:
                compressed += str(count) + prev if count > 1 else prev  # 반복된 경우 압축
                prev = current  # 현재 문자열로 업데이트
                count = 1  # 카운트 초기화

        # 남은 부분 처리
        compressed += str(count) + prev if count > 1 else prev

        # 최단 길이 갱신
        answer = min(answer, len(compressed))

    return answer
