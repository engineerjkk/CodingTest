import sys 
input = sys.stdin.readline

alpha=input().strip()
fire=input().strip()

stack=[]
for a in alpha:
    stack.append(a)
    if len(stack)>=len(fire):
        if ''.join(stack[-len(fire):])==fire:
            for _ in range(len(fire)):
                stack.pop()
if len(stack)>0:
    print(''.join(stack))
else:
    print("FRULA")