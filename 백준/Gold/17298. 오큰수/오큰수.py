import sys
input = sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))

answer = [-1]*len(numbers)
stack=[]
for i in range(len(numbers)):
    while stack and numbers[stack[-1]]<numbers[i]:
        answer[stack.pop()]=numbers[i]
    stack.append(i)
print(*answer)