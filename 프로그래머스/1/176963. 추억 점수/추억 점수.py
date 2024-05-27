def solution(name, yearning, photo):
    answer = []
    dic={}
    for key,value in zip(name,yearning):
        if key not in dic:
            dic[key]=value
        else:
            dic[key].append(value)
    
    for i in range(len(photo)):
        points=0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                points+=dic[photo[i][j]]
        answer.append(points)
                
    return answer