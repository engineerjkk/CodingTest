import sys
input = sys.stdin.readline

N,L=map(int,input().split())
signals=[]
for _ in range(N):
    signals.append(list(map(int,input().split())))

current_time=0
current_position=0
for signal in signals:
    position,red,green=signal

    move_time=position-current_position
    current_time+=move_time
    current_position=position

    cycle_time=green+red
    time_in_cycle=current_time%cycle_time

    if time_in_cycle<red:
        wait_time=red-time_in_cycle
        current_time+=wait_time

current_time+=L-current_position

print(current_time)
