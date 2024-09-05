def solution(s):
    answer = []
    string=s[2:-2].split("},{")
    total=[]
    for i in range(len(string)):
        if string[i].isdigit()==False:
            string[i]=string[i].split(',')
            tmp=[]
            for j in range(len(string[i])):
                tmp.append(int(string[i][j]))
            total.append(tmp)
        else:
            total.append([int(string[i])])
    total.sort(key=lambda x:len(x))
    for i in range(len(total)):
        for j in range(len(total[i])):
            if total[i][j] not in answer:
                answer.append(total[i][j])
    return answer