def solution(elements):
    n=len(elements)
    elements2=elements*2
    total=set()
    for i in range(n):
        summation=0
        for j in range(n):
            summation+=elements2[i+j]
            total.add(summation)
    return len(total)
