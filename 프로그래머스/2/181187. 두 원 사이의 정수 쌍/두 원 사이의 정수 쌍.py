from math import sqrt
def solution(r1, r2):
    answer=0
    for x in range(0,r1):
        y=int(sqrt(r2**2-x**2))-int(sqrt(r1**2-x**2-1))
        answer+=y
    for x in range(r1,r2):
        y=int(sqrt(r2**2-x**2))
        answer+=y
    return answer*4