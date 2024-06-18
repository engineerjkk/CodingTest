def solution(elements):
    n=len(elements)
    result=set()
    extended_elements=elements*2
    for i in range(n):
        summation=0
        for j in range(n):
            summation+=extended_elements[i+j-1]
            result.add(summation)
    return len(result)
