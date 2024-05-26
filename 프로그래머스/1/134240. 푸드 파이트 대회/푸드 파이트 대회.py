def solution(food):
    answer = ''
    left=""
    right=""
    cnt=1
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            left+=str(cnt)
        cnt+=1
    right=left[::-1]
    answer=left+"0"+right
    return answer