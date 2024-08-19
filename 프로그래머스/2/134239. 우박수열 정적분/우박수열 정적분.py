def solution(k, ranges):
    kk = [k]
    while k > 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = 3 * k + 1
        kk.append(k)
    integral = []
    for i in range(len(kk)-1):
        integral.append((kk[i] + kk[i+1])/2)
    answer = []
    for s, e in ranges:
        e = len(integral) + e
        if s == e:
            answer.append(0)
        elif s > e:
            answer.append(-1)
        else:
            answer.append(sum(integral[s:e]))
    return answer