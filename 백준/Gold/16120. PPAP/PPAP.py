import sys 
input = sys.stdin.readline 

s=input().strip()
stack=[]

for c in s:
    stack.append(c)
    if len(stack)>=4 and stack[-4:]==['P','P','A','P']:
        for i in range(4):
            stack.pop()
        stack.append('P')

if stack==['P']:
    print("PPAP")
else:
    print("NP")