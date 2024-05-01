import sys
input = sys.stdin.readline
s=list(map(str,input().strip()))

ans=[-1]*26
for i in range(len(s)):
    if ans[ord(s[i])-ord('a')] == -1:
        ans[ord(s[i])-ord('a')]=i
for i in range(len(ans)):
    print(ans[i],end=' ')