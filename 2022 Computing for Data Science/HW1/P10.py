def P10(rat_1: list, rat_2: list, measure_day: int) -> bool:  
    is_greater = 0  
    ##### Modify code Here #####
    #rat1이 rat2보다 크다면 is_greater에 True를 assign. 아니라면 False를 assign.
    if rat_1[measure_day-1] > rat_2[measure_day-1] :
        is_greater = True
    else :
        is_greater = False
    ##### End of your code #####
    return is_greater