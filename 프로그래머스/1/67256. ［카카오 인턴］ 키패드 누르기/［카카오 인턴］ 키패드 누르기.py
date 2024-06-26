def solution(numbers, hand):
    answer = ''
    keyPad={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2),0:(3,1)}
    leftPad=[1,4,7]
    rightPad=[3,6,9]
    middlePad=[2,5,8,0]
    left=(3,0)
    right=(3,2)
    for i in numbers:
        if i in leftPad:
            answer+="L"
            left=keyPad[i]
        elif i in rightPad:
            answer+="R"
            right=keyPad[i]
        else:
            r,c=keyPad[i]
            left_distance=abs(r-left[0])+abs(c-left[1])
            right_distance=abs(r-right[0])+abs(c-right[1])
            if left_distance<right_distance:
                left=(r,c)
                answer+="L"
            elif right_distance<left_distance:
                right=(r,c)
                answer+="R"
            else:
                if hand=="left":
                    left=(r,c)
                    answer+="L"
                else:
                    right=(r,c)
                    answer+="R"
                                
    return answer