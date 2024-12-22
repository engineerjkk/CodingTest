import sys
input = sys.stdin.readline

lst=input().strip()

def solution(lst):
    for i in range(len(lst)):
        if lst[i]=='@':
            robot_idx=i
        if lst[i]=='#':
            box_idx=i
        if lst[i]=='!':
            target_idx=i
    if target_idx<=robot_idx<=box_idx or box_idx<=robot_idx<=target_idx:
        return -1
    if robot_idx<=target_idx<=box_idx or box_idx<=target_idx<=robot_idx:
        return -1
    if robot_idx<=box_idx<=target_idx:
        return target_idx-robot_idx-1
    if target_idx<=box_idx<=robot_idx:
        return robot_idx-target_idx-1
    return -1

print(solution(lst))