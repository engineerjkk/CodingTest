def solution(elements):
    n=len(elements)
    elements2=elements*2
    result=set()
    for i in range(n):
        summation=0
        for j in range(n):
            summation+=elements2[i+j-1]
            result.add(summation)
    return len(result)
