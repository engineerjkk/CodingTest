def solution(price, money, count):
    answer = -1
    total=0
    for i in range(1,count+1):
        total+=price*i
    result=total-money
    if result>0:
        return result
    else:
        return 0
