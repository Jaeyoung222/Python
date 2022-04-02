def P7(L1: list) -> list:
    ans_list = []
    ##### Write your Code Here #####
    #L1의 각 item에 1을 더한 뒤 ans_list에 append
    for n in range(len(L1)) :
        ans_list.append(1+L1[n])
    ##### End of your code #####
    return ans_list