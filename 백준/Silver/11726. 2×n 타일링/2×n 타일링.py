import sys
input = sys.stdin.readline
n=int(input())
s=[0,1,2]
for i in range(3,n+1):
    a=s[-1]+s[-2]
    s.append(a%10007)
print(s[n])
