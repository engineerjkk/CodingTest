def solution(n, stations, w):
    answer = 0
    location=1
    idx=0
    while location<=n:
        if idx<len(stations) and stations[idx]-w<=location<=stations[idx]+w:
            location=stations[idx]+w+1
            idx+=1
        else:
            answer+=1
            location+=w*2+1
    return answer