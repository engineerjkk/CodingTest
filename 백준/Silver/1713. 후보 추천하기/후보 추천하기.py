import sys 
input = sys.stdin.readline
import heapq 

n=int(input())
m=int(input())
lst=list(map(int,input().split()))

dic={}
count=0
while lst:
    a=lst.pop(0)
    if a in dic:
        dic[a][0]+=1
    elif len(dic)<n:
        dic[a]=[1,count]
    else:
        max_value=1e9
        max_count=1e9
        key_idx=None
        for key, value in dic.items():
            if value[0]<max_value:
                max_value=value[0]
                max_count=value[1]
                key_idx=key
            elif value[0]==max_value and value[1]<max_count:
                max_value=value[0]
                max_count=value[1]
                key_idx=key
        del dic[key_idx]
        dic[a]=[1,count]
    count+=1

for key,(num,cnt) in sorted(dic.items(),key=lambda x:x[0]):
    print(key,end=" ")
