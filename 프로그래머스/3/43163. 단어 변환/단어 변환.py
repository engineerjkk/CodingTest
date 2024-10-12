from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    queue=deque()
    queue.append((begin,0))
    while queue:
        q,step=queue.popleft()
        if q==target:
            return step
        for i in range(len(words)):
            cnt=0
            for j in range(len(words[i])):
                if q[j]!=words[i][j]:
                    cnt+=1
            if cnt==1:
                queue.append((words[i],step+1))
                          
    
    return answer