import sys 
input = sys.stdin.readline 

n=int(input())
S=[]
for _ in range(n):
    S.append(input().strip())
S=list(set(S))

prefix=[False]*(len(S))

for i in range(len(S)):
    for j in range(len(S)):
        if i==j:
            continue
        if len(S[i])>len(S[j]):
            continue 
        if S[i]==S[j][:len(S[i])]:
            prefix[i]=True 
            break 

count=0
for i in range(len(S)):
    if not prefix[i]:
        count+=1
print(count)