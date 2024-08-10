def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            number='0'+bin(number)[2:]
            number=number[:number.rindex('0')]+'10'+number[number.rindex('0')+2:]
            answer.append(int(number,2))
    return answer