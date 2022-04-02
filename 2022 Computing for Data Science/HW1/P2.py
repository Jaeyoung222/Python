def P2(L1: list, L2: list, L3: list) -> int:
    ans = 0
    ### Modify code here ###
    ans = max(len(L1),len(L2),len(L3)) #리스트의 길이 중 최대값
    ### End of your code ###
    return ans