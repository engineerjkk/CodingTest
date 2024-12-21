import sys
input = sys.stdin.readline

def solution(h,w,blocks):
    if w<=2:
        return 0
    total_water=0
    left,right=0,w-1
    left_max,right_max=0,0
    while left<right:
        left_max=max(left_max,blocks[left])
        right_max=max(right_max,blocks[right])
        if left_max<=right_max:
            water=left_max-blocks[left]
            left+=1
        else:
            water=right_max-blocks[right]
            right-=1
        if water>0:
            total_water+=water
    return total_water


h,w=map(int,input().split())
blocks=list(map(int,input().split()))
print(solution(h,w,blocks))