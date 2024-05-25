def solution(s):
    check="0123456789"
    if len(s)==4 or len(s)==6:
        for i in s:
            if i not in check:
                return False
    else:
        return False
    return True