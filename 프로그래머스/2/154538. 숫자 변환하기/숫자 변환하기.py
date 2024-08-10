def solution(x, y, n):
    s=set()
    s.add(x)
    answer=0
    while s:
        if y in s:
            return answer
        nxt=set()
        for i in s:
            if i+n<=y:
                nxt.add(i+n)
            if i*2<=y:
                nxt.add(i*2)
            if i*3<=y:
                nxt.add(i*3)
        answer+=1
        s=nxt   
    return -1