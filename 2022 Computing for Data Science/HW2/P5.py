def P5(dct: dict) -> list:
    ### Write code here ###
    #list 2개 생성
    ans_list = []
    l1 = []
    #dct의 각 key들의 value를 중복 허락하지 않고 l1에 assign 후, 중복되는 value들은 ans_list에 assign
    for i in dct :
        if dct[i] not in l1 :
            l1.append(dct[i])
        else :
            ans_list.append(dct[i])
    return ans_list    

    ### End of your code ###     
