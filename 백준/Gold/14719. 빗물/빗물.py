import sys
input = sys.stdin.readline

def solution(h,w,blocks):
    total_water=0
    for i in range(1,w-1):
        left_max=max(blocks[:i])
        right_max=max(blocks[i+1:])
        water_level=min(left_max,right_max)
        if water_level>blocks[i]:
            total_water+=water_level-blocks[i]
    return total_water


h,w=map(int,input().split())
blocks=list(map(int,input().split()))
print(solution(h,w,blocks))