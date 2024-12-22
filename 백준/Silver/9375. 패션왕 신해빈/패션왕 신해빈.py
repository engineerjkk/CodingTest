import sys
input = sys.stdin.readline
answer=[]
t=int(input())
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
    for key, value in dic.items():
        tmp*=(len(value)+1)
    tmp-=1
    answer.append(tmp)
for i in range(t):
    print(answer[i])

        
