def solution(elements):
    n=len(elements)
    elements2=elements*2
    answer=set()
    for i in range(n):
        summation=0
        for j in range(n):
            summation+=elements2[i+j]
            answer.add(summation)
    return len(answer)