from collections import deque
def solution(numbers, hand):
    answer = ''
    dic={}
    keypad=[['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] not in dic:
                dic[keypad[i][j]]=(i,j)
    l='147'
    r='369'
    m='2580'
    l_now = "*"
    r_now = "#"
    for i in numbers:
        if str(i) in l:
            answer+='L'
            l_now=str(i)
        elif str(i) in r:
            answer+='R'
            r_now=str(i)
        elif str(i) in m:
            l_0,l_1=dic[l_now]
            r_0,r_1=dic[r_now]
            tar_0,tar_1=dic[str(i)]
            l_dis=abs(l_0-tar_0)+abs(l_1-tar_1)
            r_dis=abs(r_0-tar_0)+abs(r_1-tar_1)
            if l_dis>r_dis:
                answer+='R'
                r_now=str(i)
            elif r_dis>l_dis:
                answer+='L'
                l_now=str(i)
            else:
                if hand=="right":
                    answer+='R'
                    r_now=str(i)
                else:
                    answer+='L'
                    l_now=str(i)
            
    return answer