def solution(s):
    lst=[s[0]]
    for i in range(1,len(s)):
        if lst and lst[-1]==s[i]:
            lst.pop()
        else:
            lst.append(s[i])
    if lst:
        return 0
    else:
        return 1
