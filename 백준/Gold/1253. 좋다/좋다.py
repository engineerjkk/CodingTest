import sys
input = sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

def is_good(numbers,idx):
    target=numbers[idx]
    left=0
    right=len(numbers)-1

    while left<right:
        if left==idx:
            left+=1
            continue
        if right==idx:
            right-=1
            continue
        current_sum=numbers[left]+numbers[right]

        if current_sum==target:
            return True
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return False

cnt=0
for i in range(n):
    if is_good(numbers,i):
        cnt+=1
print(cnt)