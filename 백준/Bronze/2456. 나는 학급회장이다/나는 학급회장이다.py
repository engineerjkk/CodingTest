import sys
input = sys.stdin.readline

n=int(input())


players={}
players[1]=[0,0,0]
players[2]=[0,0,0]
players[3]=[0,0,0]
for _ in range(n):
    a,b,c=map(int,input().split())
    players[1][a-1]+=a
    players[2][b-1]+=b
    players[3][c-1]+=c

sorted_players=sorted(players.items(),key=lambda x:((x[1][0]+x[1][1]+x[1][2]),x[1][2],x[1][1],x[1][0]))

if sum(sorted_players[-1][1])>sum(sorted_players[-2][1]):
    print(sorted_players[-1][0],sum(sorted_players[-1][1]))
elif sum(sorted_players[-1][1])==sum(sorted_players[-2][1]) and sorted_players[-1][1][2]>sorted_players[-2][1][2]:
    print(sorted_players[-1][0],sum(sorted_players[-1][1]))    
elif sum(sorted_players[-1][1])==sum(sorted_players[-2][1]) and sorted_players[-1][1][2]==sorted_players[-2][1][2] and sorted_players[-1][1][1]>sorted_players[-2][1][1]:
    print(sorted_players[-1][0],sum(sorted_players[-1][1]))    
else:
    print(0,sum(sorted_players[-1][1]))
