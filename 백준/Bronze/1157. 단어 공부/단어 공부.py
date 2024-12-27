import sys
input = sys.stdin.readline

alpha=input().strip()

dic={}

for a in alpha:
    a=a.lower()
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1

answer=0
for key,value in sorted(dic.items(),key=lambda x:x[1]):
    answer=max(answer,value)

cnt=0
result=0
for key, value in dic.items():
    if value==answer:
        result=key
        cnt+=1
if cnt==1:
    print(result.upper())
else:
    print('?')