import sys 
input = sys.stdin.readline 

temperature=int(input())
initial_temperature=temperature
target_temperature=int(input())
C=int(input())
D=int(input())
E=int(input())

time=0
if initial_temperature<0:
    ice=True
else:
    ice=False
while temperature!=target_temperature:
    while temperature<0:
        time+=C
        temperature+=1
    if temperature==0 and ice:
        ice=False
        time+=D
    if not ice and temperature>=0:
        time+=E
        temperature+=1
print(time)

