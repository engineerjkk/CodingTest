def solution(s):
    dic={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    ret=""
    ans=""
    for i in s:

        if ord("0")<=ord(i)<=ord("9"):
            ans+=i
            ret=""
        else:
            ret+=i
        if len(ret)>0 and ret in dic:
            ans+=str(dic[ret])
            ret=""
    return int(ans)