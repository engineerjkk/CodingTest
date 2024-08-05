import sys
input = sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))

cnt=[0]*100001
start=0
end=0
cnt[a[start]]+=1
max_length=0
good=True
while True:
    if good:
        max_length=max(max_length,end-start+1)
        if end==n-1:
            break
        end+=1
        cnt[a[end]]+=1
        if cnt[a[end]]==k+1:
            good=False
    else:
        start+=1
        cnt[a[start-1]]-=1
        if cnt[a[start-1]]==k:
            good=True
print(max_length)

