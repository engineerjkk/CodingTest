import math
def solution(fees, records):
    answer = []
    # fees 설명
    # 기본 시간, 기본 요금 , 몇분당? , 추가요금
    basic_time , basic_fee , per_min , plus_fee = fees

    car = {}
    for idx in records:
        idx = idx.split()
        car[idx[1]] = 0

    dic = {}
    for idx in records:
        idx = idx.split()
        temp = idx[0].split(':')
        in_time = int(temp[0])*60 + int(temp[1])

        if idx[2] == 'IN':
            dic[idx[1]] = in_time

        elif idx[2] == 'OUT':
            if idx[1] in dic.keys():
                car[idx[1]] += in_time - dic[idx[1]]
                dic[idx[1]] = -1

    for key,value in dic.items():
        if value != -1: # 입차는 했는데 출차를 안한 경우임.
            car[key] = car[key] + (1439 - dic[key])


    for key,value in car.items():
        if value <= basic_time: # 기본 시간보다 아래인 누적 시간인 경우
            answer.append((int(key),basic_fee)) # 그냥 기본 요금만 받아

        elif value > basic_time: # 오버 되었으면?
            tot_fee = basic_fee + math.ceil((value - basic_time)/per_min) * plus_fee
            answer.append((int(key),tot_fee))

    answer.sort(key=lambda x : x[0]) # 차번호 기준으로 오름차순 정렬
    real_answer = []
    for key,money in answer:
        real_answer.append(money)

    return real_answer