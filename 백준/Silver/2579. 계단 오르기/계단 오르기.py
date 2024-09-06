import sys
input = sys.stdin.readline
n=int(input())
s=[]
for _ in range(n):
    s.append(int(input()))

a=[0]*n
b=[0]*n
a[0]=s[0]
b[0]=s[0]

for i in range(1,n):
    if i>=2:
        a[i]=s[i]+max(a[i-2],b[i-2])
    else:
        a[i]=s[i]
    if i>=3:
        b[i]=s[i]+s[i-1]+max(a[i-3],b[i-3])
    else:
        b[i]=s[i]+s[i-1]
print(max(a[-1],b[-1]))