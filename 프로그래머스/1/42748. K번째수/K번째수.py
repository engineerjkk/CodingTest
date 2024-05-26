def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp=[]
        for j in range(commands[i][0]-1,commands[i][1]):
            tmp.append(array[j])
        tmp.sort()
        idx=commands[i][2]-1
        answer.append(tmp[idx])
        
    return answer