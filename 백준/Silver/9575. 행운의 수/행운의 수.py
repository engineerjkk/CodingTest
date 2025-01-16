import sys 
input = sys.stdin.readline 

t=int(input())
answer=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    s=int(input())
    c=list(map(int,input().split()))
    check=['5','8']
    ans=0
    dic={}
    for i in range(n):
        for j in range(m):
            for k in range(s):
                tmp=a[i]+b[j]+c[k]
                tmp=str(tmp)
                flag=True 
                for t in tmp:
                    if t not in check:
                        flag=False
                        break 
                if flag:
                    if tmp not in dic:
                        dic[tmp]=1
                    else:
                        dic[tmp]+=1
    answer.append(len(dic))
for i in answer:
    print(i)
