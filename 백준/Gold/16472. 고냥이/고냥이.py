import sys
input = sys.stdin.readline

n=int(input())
s=input().strip()

count=[0]*26
num_types=0

start=0
end=0
count[ord(s[0])-ord('a')]=1
num_types=1

answer=0
while start<len(s) and end<len(s):
    if num_types<=n:
        answer=max(answer,end-start+1)
        end+=1
        if end<len(s):
            count[ord(s[end])-ord('a')]+=1
            if count[ord(s[end])-ord('a')]==1:
                num_types+=1
    else:
        start+=1
        count[ord(s[start-1])-ord('a')]-=1
        if count[ord(s[start-1])-ord('a')]==0:
            num_types-=1

print(answer)