import sys 
input = sys.stdin.readline 

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    current_arr=arr[0]
    max_arr=arr[0]

    for num in arr[1:]:
        current_arr=max(num,current_arr+num)
        max_arr=max(max_arr,current_arr)
    
    print(max_arr)