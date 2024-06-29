import sys
input = sys.stdin.readline
n=int(input())
m=int(input())
s=str(input())

value="I"
for i in range(n):
    value+="OI"
len_value=len(value)
cnt=0
for i in range(m-len_value+1): 
    a=s[i:i+len_value]
    if a==value:
        cnt+=1
print(cnt)
