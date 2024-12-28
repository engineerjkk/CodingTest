import sys
input = sys.stdin.readline

dr=[-1,0,1,0]
dc=[0,1,0,-1]

class Turtle:
    def __init__(self,r,c,d):
        self.r=r
        self.c=c
        self.d=d
    def go(self):
        self.r+=dr[self.d]
        self.c+=dc[self.d]
    def back(self):
        self.r-=dr[self.d]
        self.c-=dc[self.d]
    def left(self):
        self.d=(self.d+3)%4
    def right(self):
        self.d=(self.d+1)%4

t=int(input())
for _ in range(t):
    orders=input().strip()
    visit=[(0,0)]
    turtle=Turtle(0,0,0)
    for order in orders:
        if order=='F':
            turtle.go()
        elif order=='B':
            turtle.back()
        elif order=='L':
            turtle.left()
        else:
            turtle.right()
        visit.append((turtle.r,turtle.c))

    min_r=min([v[0] for v in visit])
    max_r=max([v[0] for v in visit])
    min_c=min([v[1] for v in visit])
    max_c=max([v[1] for v in visit])

    width=max_c-min_c
    height=max_r-min_r
    area=width*height
    print(area)
    
