import sys 
input = sys.stdin.readline 

t=int(input())
for _ in range(t):
    d,n=map(int,input().split())
    lst=list(map(int,input().split()))

    remainder_count=[0]*d 
    remainder_count[0]=1

    curr_sum=0
    count=0
    for num in lst:
        curr_sum=(curr_sum+num)%d
        count+=remainder_count[curr_sum]
        remainder_count[curr_sum]+=1
    print(count)