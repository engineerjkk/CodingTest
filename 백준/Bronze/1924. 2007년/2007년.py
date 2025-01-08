import sys 
input = sys.stdin.readline 

target_mon,target_day=map(int,input().split())
month=[31,28,31,30,31,30,31,31,30,31,30,31]
weeks=['SUN','MON','TUE','WED','THU','FRI','SAT']

mon=0
day=1
we=1
while True:
    if day>month[mon]:
        mon+=1
        day=1
    if we>6:
        we=0
    if target_mon-1==mon and target_day == day:
        break
    day+=1 
    we+=1
print(weeks[we])