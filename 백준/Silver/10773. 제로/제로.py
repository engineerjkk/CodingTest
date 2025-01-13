import sys 
input = sys.stdin.readline 

k=int(input())
stack=[]
for _ in range(k):
    n=int(input())
    if stack and n==0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))