def solution(elements):
    answer = 0
    
    li = list()
    for k in range(len(elements)):
        i = 0
        j = k + 1
        for _ in range(len(elements)):
            if (j >= len(elements)):
                li.append(sum(elements[i : ]) + sum(elements[ : j - len(elements)]))
            else:
                li.append(sum(elements[i : j]))

            i += 1
            j += 1
    
    answer = len(set(li))

    return answer