def solution(genres, plays):
    answer = []
    dic1={}
    for i in range(len(genres)):
        if genres[i] not in dic1:
            dic1[genres[i]]=[(plays[i],i)]
        else:
            dic1[genres[i]].append((plays[i],i))
    dic2={}
    for i in range(len(genres)):
        if genres[i] not in dic2:
            dic2[genres[i]]=plays[i]
        else:
            dic2[genres[i]]+=plays[i]
    print(dic1)
    print(dic2)
    for key,value in sorted(dic2.items(),key=lambda x:x[1],reverse=True):
        for i,p in enumerate(sorted(dic1[key],key=lambda x:x[0], reverse=True)[:2]):
            answer.append(p[1])
    return answer