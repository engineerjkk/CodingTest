def solution(land):
    # 두 번째 행부터 마지막 행까지 순회합니다.
    for i in range(1, len(land)):
        # 각 행의 열을 순회합니다.
        for j in range(len(land[0])):
            # 현재 위치의 값에 이전 행에서 현재 열을 제외한 열들 중 최대값을 더합니다.
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    # 마지막 행에서 가장 큰 값을 반환합니다.
    return max(land[len(land) - 1])