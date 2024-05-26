def solution(s):
    answer = 0
    lst_chr=["zero","one","two","three","four","five","six","seven","eight","nine"]
    lst_int="0123456789"
    answer=""
    tmp=""
    answer=""
    for i in s:
        if ord('a')<=ord(i)<=ord('z'):
            tmp+=i
            if tmp in lst_chr:
                answer+=str(lst_chr.index(tmp))
                tmp=""
        else:
            answer+=i
            
    return int(answer)