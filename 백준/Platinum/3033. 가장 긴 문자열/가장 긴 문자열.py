import sys
input = sys.stdin.readline
n=int(input())
s=str(input())

mod=1e9+7
po=[0]*n
po[0]=1
for i in range(1,n):
    po[i]=(po[i-1]*31)%mod

left=1
right=n-1
answer=0
while left<=right:
    mid=(left+right)//2
    found=False

    hash=0
    for i in range(mid):
        hash*=31
        hash%=mod
        hash+=ord(s[i])-ord("a")+1
        hash%=mod
    
    check={}
    for i in range(n-mid+1):
        if hash in check:
            for j in check[hash]:
                if s[j:j+mid]==s[i:i+mid]:
                    found=True
                    break
            check[hash].append(i)
            if found:
                break
        else:
            check[hash]=[i]
        hash-=((ord(s[i])-ord("a")+1)*po[mid-1])%mod
        hash*=31
        hash%=mod
        hash+=(ord(s[i+mid])-ord("a")+1)
        hash%=mod

    if found:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)