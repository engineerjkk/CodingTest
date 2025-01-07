import sys 
input = sys.stdin.readline 

n=int(input())
lst=list(map(int,input().split()))

total=sum(lst)

a=max(lst)

if total !=1 and a>total/2:
    print("Unhappy")
else:
    print("Happy")