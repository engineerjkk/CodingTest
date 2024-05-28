from collections import deque
def solution(ingredient):
    
    s=[]
    answer=0
    for i in ingredient:
        s.append(i)
        if len(s)>=4 and s[-4:]==[1,2,3,1]:
            answer+=1
            for _ in range(4):
                s.pop()
    return answer
