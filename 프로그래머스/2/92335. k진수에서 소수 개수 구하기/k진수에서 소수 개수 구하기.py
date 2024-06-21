def to_k_number(n, k):
    # n을 k진수로 변환하는 함수
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n // k
    return ''.join(reversed(ret))

def is_prime_num(k):
    # 주어진 숫자가 소수인지 확인하는 함수
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    # n을 k진수로 변환
    k_num = to_k_number(n, k)
    # 0을 기준으로 문자열을 나누어 소수 후보들 추출
    for num in k_num.split('0'):
        if num == "":
            continue
        # 각 num이 소수인지 판별
        if is_prime_num(int(num)):
            answer += 1
    return answer
