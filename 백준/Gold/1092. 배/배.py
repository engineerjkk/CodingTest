def min_time_to_move_boxes(N, cranes, M, boxes):
    # 내림차순으로 정렬
    cranes.sort(reverse=True)
    boxes.sort(reverse=True)
    
    # 가장 무거운 박스가 가장 큰 크레인 용량보다 크면 불가능
    if boxes[0] > cranes[0]:
        return -1
    
    # 남은 박스를 저장할 리스트
    remaining_boxes = boxes[:]
    time = 0
    
    # 모든 박스를 옮길 때까지 반복
    while remaining_boxes:
        time += 1
        box_idx = 0
        
        # 각 크레인에 대해
        for crane in cranes:
            # 남은 박스가 없으면 break
            if box_idx >= len(remaining_boxes):
                break
                
            # 현재 크레인으로 들 수 있는 가장 무거운 박스 찾기
            while box_idx < len(remaining_boxes):
                if remaining_boxes[box_idx] <= crane:
                    remaining_boxes.pop(box_idx)
                    break
                box_idx += 1
    
    return time

# 입력 처리
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

# 결과 출력
print(min_time_to_move_boxes(N, cranes, M, boxes))