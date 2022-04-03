def P4(dct: dict) -> str:
    ### Write code here ###
    #string을 생성하고, dct의 value 중 최대값을 variable(atom)에 assign
    ans = ""
    atom = max(dct.values())
    #dct의 key들 중 atom의 값을 value로 같는 key를 ans에 assign
    for i in dct.keys() :
        if dct[i] == atom :
            ans = i
    return ans
    ### End of your code ###     
