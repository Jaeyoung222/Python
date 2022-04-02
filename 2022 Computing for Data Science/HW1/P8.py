from typing import List
def P8(num_list: List[float]):
    ans_list = []
    ##### Modify code Here #####
    #num_list의 각 item이 0이상인지 검사 후 ans_list에 append
    for n in range(len(num_list)) :
        if num_list[n] >= 0 :
            ans_list.append(num_list[n])
    ##### End of your code #####
    return ans_list
    

