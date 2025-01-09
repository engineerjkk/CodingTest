import sys 
input = sys.stdin.readline 

n=int(input())
s=[]
for _ in range(n):
    s.append(input().strip())
s=list(set(s))

prefix=[False]*len(s)

for i in range(len(s)):
    for j in range(len(s)):
        if i==j:
            continue 
        if len(s[i])>=len(s[j]):
            continue
        if s[i]==s[j][:len(s[i])]:
            prefix[i]=True
            break 

count=0
for i in range(len(s)):
    if not prefix[i]:
        count+=1 
print(count)