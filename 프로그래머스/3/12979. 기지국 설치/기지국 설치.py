def solution(n, stations, w):
    ans=0
    idx=0
    location=1
    while location<=n:
        # 기지국 범위에 있을 때
        if idx<len(stations) and stations[idx]-w<=location<=stations[idx]+w:
            location=stations[idx]+w+1
            idx+=1
        # 기지국 범위 밖일 때
        else:
            location+=w*2+1
            ans+=1
        
        
    return ans      
