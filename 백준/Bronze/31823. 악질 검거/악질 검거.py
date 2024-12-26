import sys 
input = sys.stdin.readline

n,m=map(int,input().split())

lst=[]
dic={}
for _ in range(n):
    tmp=list(map(str,input().split()))
    name=tmp[-1]
    strick=tmp[:-1]
    MAX=0
    cnt=0
    for i in strick:
        if i=='*':
            cnt=0
            continue
        elif i=='.':
            cnt+=1
        MAX=max(MAX,cnt)
    dic[name]=MAX
#sorted_dic=sorted(dic.items(),key=lambda x:x[1])
tmp=set()
for key, value in dic.items():
    tmp.add(value)
print(len(tmp))

for key,value in dic.items():
    print(value,key)