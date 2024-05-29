def solution(n):
    answer = 0
    m=n
    while True:
        m+=1
        if str(bin(n)[2:]).count("1")==str(bin(m)[2:]).count("1"):
            return m