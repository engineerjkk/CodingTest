def solution(numbers):
    lst=[]
    for i in range(10):
        if i not in numbers:
            lst.append(i)
            
    
    
    return sum(lst)