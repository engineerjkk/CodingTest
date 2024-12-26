import sys
input = sys.stdin.readline

answer=[
    ['d','d','d'],
    ['d','c','b'],
    ['d','b','a']
    ]

for _ in range(4):
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    if x2<x3 or x4<x1:
        x_intersection=0
    elif x2==x3 or x4==x1:
        x_intersection=1
    else:
        x_intersection=2
    if y2<y3 or y4<y1:
        y_intersection=0
    elif y2==y3 or y4==y1:
        y_intersection=1
    else:
        y_intersection=2
    print(answer[x_intersection][y_intersection])
