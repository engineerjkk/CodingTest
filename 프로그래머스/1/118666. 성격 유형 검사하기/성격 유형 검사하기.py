def solution(survey, choices):
    answer = ''
    dic={"RT":0,"CF":0,"JM":0,"AN":0}
    for s,c in zip(survey,choices):
        if s in ["TR","FC","MJ","NA"]:
            s=s[::-1]
            c=8-c
        c-=4
        dic[s]+=c
        
    
    for key,value in dic.items():
        if value<0:
            answer+=key[0]
        elif value>0:
            answer+=key[1]
        else:
            key=list(key)
            answer+=sorted(key)[0]
    
    return answer