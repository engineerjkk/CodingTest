def solution(s):
    answer = -1
    tmp=[ord(s[0])]
    s=s[1:]
    ord_s=[]
    for i in s:
        ord_s.append(ord(i))
    
    for i in ord_s:
        if len(tmp)>0:
            if tmp[-1]==i:
                tmp.pop()
            else:
                tmp.append(i)
        else:
            tmp.append(i)
                
    if len(tmp)==0:
        return 1
    else:
        return 0
