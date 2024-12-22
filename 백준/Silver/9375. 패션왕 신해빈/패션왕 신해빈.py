import sys
input = sys.stdin.readline

t=int(input())
answer=[]
for _ in range(t):
    n=int(input())
    dic={}
    for _ in range(n):
        product,category=input().split()
        if category not in dic:
            dic[category]=[product]
        else:
            dic[category].append(product)
    tmp=1
    for category,product in dic.items():
        tmp*=(len(product)+1)
    tmp-=1
    answer.append(tmp)
for i in range(t):
    print(answer[i])
