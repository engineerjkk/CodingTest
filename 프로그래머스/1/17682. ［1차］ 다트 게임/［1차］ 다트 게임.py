def solution(dartResult):
    result=[]
    num=""
    for i in dartResult:
        if i.isdecimal():
            num+=i
        elif i.isalpha():
            result.append(int(num))
            num=""
            if i=="D":
                result[-1]=result[-1]**2
            elif i=="T":
                result[-1]=result[-1]**3
        else:
            if i=="*":
                result[-1]=result[-1]*2
                if len(result)>1:
                    result[-2]=result[-2]*2
            elif i=="#":
                result[-1]=-result[-1]
    return sum(result)
