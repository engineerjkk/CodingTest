import sys
input = sys.stdin.readline

n = int(input())
dic = {}

# 마지막 로그 상태만 저장
for _ in range(n):
    name, log = input().split()
    dic[name] = log  # 각 사람의 마지막 상태만 저장

# 현재 회사에 있는 사람만 필터링하고 역순 정렬
answer = []
for name, log in dic.items():
    if log == 'enter':
        answer.append(name)

# 사전 순의 역순으로 정렬
answer.sort(reverse=True)

# 결과 출력
for name in answer:
    print(name)