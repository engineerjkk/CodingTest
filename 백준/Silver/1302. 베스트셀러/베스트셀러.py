import sys
input = sys.stdin.readline

n=int(input())
dic={}
for _ in range(n):
    s=input().strip()
    if s not in dic:
        dic[s]=1
    else:
        dic[s]+=1
sorted_dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
answer=[]
num=sorted_dic[0][1]
for key,value in sorted_dic:
    if value==num:
        answer.append(key)
answer.sort()
print(answer[0])