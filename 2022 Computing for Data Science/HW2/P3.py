def P3(dct: dict) -> int:
    ### Write code here ###
    #dct의 value들로 집합을 만들고 그 길이를 return
    ans = len(set(dct.values()))
    return ans
    ### End of your code ###     
