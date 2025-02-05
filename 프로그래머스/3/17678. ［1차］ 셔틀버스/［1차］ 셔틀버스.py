def solution(n, t, m, asdasd):
    answer = 0
    timetable = []
    for i in asdasd:
        aa = i.split(":")
        s = int(aa[0])*60 + int(aa[1])
        timetable.append(s)
    timetable.sort()
    
    start = 540 
    lt = len(timetable)
    crew = 0
    for i in range(n):
        passenger = 0	
        while (passenger < m):
            if (crew < lt and timetable[crew] <= start):
                crew += 1
                passenger += 1
            else:
                break
        if (passenger == m):
            answer = timetable[crew-1]-1
        if (passenger < m):
            answer = start
        start += t
    a = str(answer//60) if answer//60 >= 10 else "0"+str(answer//60)
    b = str(answer % 60) if answer % 60 >= 10 else "0"+str(answer % 60)
    result = a+":"+b

    return result