
def move(r,c,board):
    n=len(board)
    while r<n:
        if board[r][c]!=0:
            caught_doll=board[r][c]
            board[r][c]=0
            return caught_doll
        r+=1

def solution(board, moves):
    answer = 0
    busket=[]
    for c in moves:
        c-=1
        doll=move(0,c,board)
        if len(busket)>0 and busket[-1]==doll:
            busket.pop()
            answer+=2
        else:
            if doll != None:
                busket.append(doll)
        
    return answer