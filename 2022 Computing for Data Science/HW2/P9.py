def P9(dct1: dict, dct2: dict) -> int: 
    ### Write code here ###
    #variable 생성
    ans = 0
    #dct1의 key가 dct2에 존재하는지 검사하고 있다면 그 key에 해당하는 dct1과 dct2의 value를 곱해서 ans에 더함.
    for key in dct1 :
        if key in dct2 :
            ans += dct1[key]*dct2[key]
            
    return ans

    ### End of your code ###    
