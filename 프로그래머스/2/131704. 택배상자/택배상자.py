def solution(order):
    answer = 0
    n=len(order)
    idx=0
    i=1
    stack=[]
    while i<n+1:
        stack.append(i)
        while stack[-1]==order[idx]:
            stack.pop()
            idx+=1
            if len(stack)==0:
                break
        i+=1
    return idx