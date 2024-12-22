def solve_kindergarten(N, K, heights):
    # 인접한 원생들의 키 차이를 계산
    differences = []
    for i in range(N-1):
        diff = heights[i+1] - heights[i]
        differences.append(diff)
    
    # 차이를 내림차순으로 정렬
    differences.sort(reverse=True)
    
    # 가장 큰 차이 K-1개를 선택하여 그룹을 나눔
    # 전체 키 차이에서 선택된 차이들을 제외한 값이 답
    total_diff = heights[-1] - heights[0]  # 전체 키 차이
    sum_excluded = sum(differences[:K-1])  # 제외할 차이들의 합
    
    return total_diff - sum_excluded

# 입력 처리
N, K = map(int, input().split())
heights = list(map(int, input().split()))

# 결과 출력
result = solve_kindergarten(N, K, heights)
print(result)