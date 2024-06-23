def solution(msg):
    dic={}
    for i in range(26):
        dic[chr(ord("A")+i)]=i+1
    w,c=0,0
    answer=[]
    while True:
        c+=1
        if c==len(msg):
            answer.append(dic[msg[w:c+1]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]]=len(dic)+1
            answer.append(dic[msg[w:c]])
            w=c
    return answer
        