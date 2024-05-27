def solution(a, b):
    answer = ''
    WoD=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    Month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    idx=5
    d=1
    m=1
    while True:
        if m==a and d==b:
            answer=WoD[idx]
            break
        d+=1
        idx+=1
        if d>Month[m]:
            m+=1
            d=1
        if idx>6:
            idx=0
        answer=WoD[idx]
    
    return answer