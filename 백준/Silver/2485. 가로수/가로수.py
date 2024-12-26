import sys
input = sys.stdin.readline

n=int(input())
lst=[0]*n
for i in range(n):
    lst[i]=int(input())

def gcd(a,b):
    if a<b:
        b,a=a,b
    if b==0:
        return a
    else:
        return gcd(b,a%b)

d=0
for i in range(n-1):
    d=gcd(d,(lst[i+1]-lst[i]))

print((lst[-1]-lst[0])//d+1-n)
