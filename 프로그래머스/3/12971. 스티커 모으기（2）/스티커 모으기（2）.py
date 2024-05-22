def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    # 첫 번째 스티커를 선택하는 경우
    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    # 첫 번째 스티커를 선택하지 않는 경우
    dp2 = [0] * len(sticker)
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    # 최종 결과 반환
    return max(dp1[len(sticker) - 2], dp2[len(sticker) - 1])
