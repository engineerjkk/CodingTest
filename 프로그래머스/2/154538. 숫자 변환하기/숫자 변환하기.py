def solution(x, y, n):
    inf=1e9
    dp = [inf for _ in range(3*y+1)]
    dp[x] = 0

    for i in range(x, y+1):

        dp[i+n] = min(dp[i+n], dp[i]+1)
        dp[i*2] = min(dp[i*2], dp[i]+1)
        dp[i*3] = min(dp[i*3], dp[i]+1)

    #print(dp)
    return dp[y] if dp[y] < 1000000 else -1