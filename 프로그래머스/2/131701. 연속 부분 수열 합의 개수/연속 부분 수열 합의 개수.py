def solution(elements):
    n=len(elements)
    answer=set()
    elements2=elements*2
    for i in range(n):
        total=0
        for j in range(n):
            total+=elements2[i+j]
            answer.add(total)
    return len(answer)
