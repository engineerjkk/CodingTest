def solution(s):
    dic={}
    answer=[]
    for i,v in enumerate(s):
        if v not in dic:
            dic[v]=i
            answer.append(-1)
        else:
            answer.append(i-dic[v])
            dic[v]=i
    return answer