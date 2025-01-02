import sys
input = sys.stdin.readline

t=int(input())
count=0
for _ in range(t):
    alpha=input().strip()
    stack=[]
    for a in alpha:
        if len(stack)==0 or stack[-1]!=a:
            stack.append(a)
        else:
            stack.pop()
    if len(stack)==0:
        count+=1
print(count)