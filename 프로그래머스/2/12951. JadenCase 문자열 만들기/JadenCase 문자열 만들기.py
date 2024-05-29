def solution(s):
    S=" "+s
    answer=""
    " AAAA"
    cnt=0
    for i,string in enumerate(S):
        if string.isspace():
            answer+=string
            cnt=0
        elif cnt==0 and string.islower():
            answer+=string.upper()
            cnt+=1
        elif cnt==0 and string.isupper():
            answer+=string
            cnt+=1
        else:
            answer+=string.lower()
            cnt+=1
    return answer[1:]