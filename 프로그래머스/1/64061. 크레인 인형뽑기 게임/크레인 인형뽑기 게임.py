def solution(board, moves):
    answer=0
    def space(board,j):
        for i in range(len(board)):
            if board[i][j-1] !=0:
                doll=board[i][j-1]
                board[i][j-1] =0
                return board,True,doll
        return board,False,False
    s=[]
    for j in moves:
        board,check,doll=space(board,j)
        if check:
            s.append(doll)
            while True:
                if len(s)>=2:
                    if s[-2]==s[-1]:
                        s.pop()
                        s.pop()
                        answer+=2
                    else:
                        break
                else:
                    break
    return answer