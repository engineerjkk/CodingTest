import sys
input = sys.stdin.readline

n=int(input())
string=input().strip()

answer=0
for i,alpha in enumerate(string):
    answer+=(ord(alpha)-ord('a')+1)*(31**i)
print(answer%1234567891)