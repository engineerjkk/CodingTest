import sys
input = sys.stdin.readline
n=int(input())
s=str(input())

T=""
for i in range(n):
    if i==0 or s[i] !=s[i-1]:
        T+=s[i]

blue=0
red=0
for i in range(len(T)):
    if T[i]=="B":
        blue+=1
    else:
        red+=1
if blue<red:
    print(1+blue)
else:
    print(1+red)