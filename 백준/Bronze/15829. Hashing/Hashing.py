import sys
input = sys.stdin.readline

n=int(input())
string=input().strip()

myhash=[31]*26

answer=0
for i,alpha in enumerate(string):
    answer+=(ord(alpha)-ord('a')+1)*(31**i)
print(answer)