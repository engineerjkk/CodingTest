def can_cross(stones, k, people):
    # stones 배열을 복사하여 사용
    temp = stones
    
    # 연속된 0의 개수를 세는 변수
    zero_count = 0
    
    # 모든 돌을 확인
    for i in range(len(temp)):
        # 현재 돌에서 people만큼의 인원이 건넌 후의 값 계산
        if temp[i] < people:
            zero_count += 1
        else:
            zero_count = 0
            
        # 연속된 0의 개수가 k를 초과하면 건널 수 없음
        if zero_count >= k:
            return False
    
    return True

def solution(stones, k):
    # 이진 탐색을 위한 left, right 설정
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid명이 건널 수 있는지 확인
        if can_cross(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right

# # 테스트
# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# k = 3
# print(solution(stones, k))  # 3