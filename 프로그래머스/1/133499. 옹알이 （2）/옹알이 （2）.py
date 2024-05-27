def solution(babbling):
    pron=["aya", "ye", "woo", "ma"]
    answer=0
    for i in babbling:
        for j in pron:
            if j*2 not in i:
                i=i.replace(j," ")
        if i.isspace():
            answer+=1
    return answer