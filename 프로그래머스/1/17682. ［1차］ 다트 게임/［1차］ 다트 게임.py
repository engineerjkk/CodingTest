def solution(dartResult):
    result=[]
    stack=[]
    i=0
    num=""
    for i in dartResult:
        if i.isdecimal():
            num+=i
        if i.isalpha():
            result.append(int(num))
            num=""
            if i=="D":
                result[-1]=result[-1]**2
            elif i=="T":
                result[-1]=result[-1]**3
            continue
        else:
            if i=="*":
                if len(result)>1:
                    result[-1]=result[-1]*2
                    result[-2]=result[-2]*2
                elif len(result)==1:
                    result[-1]=result[-1]*2
            elif i=="#":
                result[-1]=-result[-1]
            continue
        
    return int(sum(result))