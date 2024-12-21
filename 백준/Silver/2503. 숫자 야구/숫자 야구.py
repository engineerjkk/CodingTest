import sys
input = sys.stdin.readline
from itertools import permutations
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

a=['1','2','3','4','5','6','7','8','9']

def func(combi,lst):
    num,strike,ball=lst
    num=str(num)
    tmp_strike=0
    tmp_ball=0
    for a,b in zip(combi,num):
        if a==b:
            tmp_strike+=1
        else:
            if b in combi:
                tmp_ball+=1
    return strike==tmp_strike and ball==tmp_ball

answer=[]
for combi in permutations(a,3):
    combi=''.join(combi)
    result=True
    for i in range(len(lst)):
        if not func(combi,lst[i]):
            result=False
            break
    if result:
        tmp=''
        for j in combi:
            tmp+=j
        answer.append(int(tmp))
print(len(answer))