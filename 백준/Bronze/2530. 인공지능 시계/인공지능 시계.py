import sys
input = sys.stdin.readline

hour,minute,sec=map(int,input().split())
time=int(input())


while time!=0:
    sec+=1
    time-=1
    if sec==60:
        sec=0
        minute+=1
    if minute==60:
        minute=0
        hour+=1
    if hour==24:
        hour=0
        minute=0
        sec=0
    
print(hour,minute,sec)