def P8(dct: dict) -> bool:
    ### Write code here ###
    #variable 생성
    ans = 0
    #R,G,B의 value들을 더하고 1이면 ans에 True를 assign, 아니면 False를 assign
    if dct['R'] + dct['G'] + dct['B'] == 1 :
        ans = True
    else :
        ans = False
    return ans

    ### End of your code ###    
