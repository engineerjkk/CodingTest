def solution(survey, choices):
    c=[3,2,1,0,1,2,3]
    dic={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    check=["RT","CF","JM","AN"]
    answer=""
    for i,j in zip(survey,choices):
        point=j-1
        if point ==3:
            continue
        elif point <3:
            dic[i[0]]+=c[point]
        else:
            dic[i[1]]+=c[point]
    for i in check:
        if dic[i[0]]>dic[i[1]]:
            answer+=i[0]
        elif dic[i[1]]>dic[i[0]]:
            answer+=i[1]
        else:
            answer+=sorted(i)[0]

    return answer

'''
    c=[3,2,1,0,1,2,3]
    s=["R","T","C","F","J","M","A","N"]
    dic={"RT":[0,0],"CF":[0,0],"JM":[0,0],"AN":[0,0]}
    for i,j in zip(survey,choices):
        point=j-1
        if point ==3:
            continue
        elif point <3:
            dic[i][0]+=c[point]
        else:
            dic[i][1]+=c[point]
    answer=""
    for key,value in dic.items():
        if value[0]>value[1]:
            answer+=key[0]
        elif value[1]>value[0]:
            answer+=key[1]
        else:
            answer+=sorted(key)[0]'''