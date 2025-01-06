import sys 
input = sys.stdin.readline 

t=int(input())

def max_subarray(arr):
    max_sum=arr[0]
    current_sum=arr[0]

    for num in arr[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum

for _ in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    print(max_subarray(lst))
