from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    queue=deque()
    queue.append((begin,0))
    while queue:
        now,step=queue.popleft()
        if now==target:
            return step
        for i in range(len(words)):
            cnt=0
            for j in range(len(words[i])):
                if now[j]!=words[i][j]:
                    cnt+=1
            if cnt==1:
                queue.append((words[i],step+1))
                       
    return 0