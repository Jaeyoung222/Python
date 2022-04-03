def P6(dct1: dict, dct2: dict) -> dict:
    ### Write code here ###
    #dictionary 생성
    ans_d = {}
    #dct1의 각 key가 dct2에 존재하는지 찾고, 그 key의 dct2에서의 value가 dct1의 value와 같으면 ans_d에 assign
    for key in dct1 :
        if (key in dct2) and (dct1[key] == dct2[key]) :
            ans_d[key] = dct1[key]
    return ans_d
    ### End of your code ###     
