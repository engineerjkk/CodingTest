def solution(s, t):
    # s를 t의 길이만큼, t를 s의 길이만큼 반복하여 비교
    # 이렇게 하면 두 문자열의 최소공배수 길이까지 패턴이 같은지 확인할 수 있음
    s_repeated = s * len(t)
    t_repeated = t * len(s)
    
    # 두 문자열이 같으면 1, 다르면 0 반환
    return 1 if s_repeated == t_repeated else 0

# 입력 받기
s = input().strip()
t = input().strip()

# 결과 출력
print(solution(s, t))