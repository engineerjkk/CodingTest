def solution(dartResult):
    answer = 0
    lst=[]
    num=0
    dartResult=dartResult.replace("10","-")
    for i,v in enumerate(list(dartResult.strip())):
        if ord('0')<=ord(v)<=ord('9'):
            num=int(v)
        elif v=="-":
            num=10
        elif v=="S":
            tmp=num
            lst.append(tmp)
        elif v=="D":
            tmp=num**2
            lst.append(tmp)
        elif v=="T":
            tmp=num**3
            lst.append(tmp)
        elif v=="#":
            lst[-1]=lst[-1]*(-1)
        elif v=="*":
            if len(lst)>=2:
                lst[-2]=lst[-2]*2
                lst[-1]=lst[-1]*2
            else:
                lst[-1]=lst[-1]*2
    print(lst)
    return sum(lst)