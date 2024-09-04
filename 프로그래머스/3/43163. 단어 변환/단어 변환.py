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
        for word in words:
            cnt=0
            for i in range(len(word)):
                if q[i]!=word[i]:
                    cnt+=1
            if cnt==1:
                queue.append((word,step+1))
    return answer