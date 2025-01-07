import sys 
input= sys.stdin.readline 

S=input().strip()
power=1
answer=0
mod=int(1e9+7)
for i in range(len(S)):
    if S[i]=='O':
        answer+=power
        answer%=mod
    power*=2
    power%=mod
print(answer)