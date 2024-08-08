def solution(x, y, n):
    answer = 0
    s=set()
    s.add(x)
    while s:
        if y in s:
            return answer
        nxt_set=set()
        for i in s:
            if i+n <=y:
                nxt_set.add(i+n)
            if i*2<=y:
                nxt_set.add(i*2)
            if i*3<=y:
                nxt_set.add(i*3)
        s=nxt_set
        answer+=1
    return -1