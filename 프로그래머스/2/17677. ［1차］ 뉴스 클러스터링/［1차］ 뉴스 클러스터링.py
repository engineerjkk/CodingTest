def checklist(strin):
    arr=[]
    for b in range(len(strin) - 1):
        s = strin[b]+strin[b + 1]
        if s.isalpha():
            arr.append(s)
            #print(arr)
    return arr

def solution(str1, str2):
    str1, str2 = checklist(str1.upper()), checklist(str2.upper())
    union, intersection = [], []
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    for a in str1:
        if a in str2:
            str2.remove(a)
            intersection.append(a)
    union = str1 + str2
    if len(union) == 0:
        return 65536
    return int((len(intersection) / len(union)) * 65536)