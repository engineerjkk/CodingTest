def solution(strings, n):
    answer = []
    dic={}
    for s in strings:
        if s not in dic:
            dic[s]=s[n]
    dic=sorted(dic.items(),key = lambda x:(x[1],x[0]))
    for key,value in dic:
        answer.append(key)
           
           
    return answer