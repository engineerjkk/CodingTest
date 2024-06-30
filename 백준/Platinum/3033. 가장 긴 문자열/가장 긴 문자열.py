L=int(input())
S=input()

mod=1e9+7
po=[0]*L
po[0]=1
for i in range(1,L):
    po[i]=po[i-1]*31%mod

low=1
high=L-1
answer=0

while low<=high:
    mid=(low+high)//2
    found=False

    # 가장 앞에 있는 길이 mid인 부분 문자열의 해쉬값
    hash=0
    for i in range(mid):
        hash*=31
        hash%=mod
        hash+=ord(S[i])-ord('a')+1
        hash%=mod
    check={}

    for i in range(0,L-mid+1):
        #S[i:i+mid] 문자열의 해쉬값을 체크
        if hash in check:
            for j in check[hash]:
                if S[j:j+mid]==S[i:i+mid]:
                    found=True
                    break
            check[hash].append(i)
            if found:
                break
        else:
            check[hash]=[i]

        #해쉬값을 갱신
        hash+=mod-(ord(S[i]) - ord("a")+1)*po[mid-1]
        hash*=31
        hash%=mod
        if i+mid<L:
            hash+=ord(S[i+mid])-ord("a")+1
            hash%=mod

    if found:
        answer=mid
        low=mid+1
    else:
        high=mid-1

print(answer)