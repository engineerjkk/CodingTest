def solution(n, stations, w):
    idx=0
    current=1
    answer=0
    while current<=n:
        if idx<len(stations) and stations[idx]-w<=current<=stations[idx]+w:
            current=stations[idx]+w+1
            idx+=1
        else:
            current+=2*w+1
            answer+=1
    return answer