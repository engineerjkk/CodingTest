def solution(enroll, referral, seller, amount):
    # 판매원들의 정보를 저장할 딕셔너리 생성
    # key: 판매원 이름, value: [추천인, 총 수익]
    sales_info = {}
    
    # 초기 판매원 정보 설정
    for i in range(len(enroll)):
        sales_info[enroll[i]] = [referral[i], 0]
    
    # 판매 기록을 순회하며 수익 분배
    for i in range(len(seller)):
        current_seller = seller[i]
        profit = amount[i] * 100  # 칫솔 한 개당 100원
        
        # 수익 분배 처리
        while current_seller != "-" and profit > 0:
            # 현재 판매원의 수익 계산 (90%)
            current_profit = profit - (profit // 10)
            sales_info[current_seller][1] += current_profit
            
            # 추천인에게 분배될 수익 계산 (10%)
            profit = profit // 10
            
            # 1원 미만인 경우 더 이상 분배하지 않음
            if profit == 0:
                break
                
            # 다음 추천인으로 이동
            current_seller = sales_info[current_seller][0]
    
    # 결과 배열 생성
    result = []
    for name in enroll:
        result.append(sales_info[name][1])
    
    return result