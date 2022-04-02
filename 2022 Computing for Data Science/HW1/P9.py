def P9(nested_list: list) -> list:    
    ans_list = []
    ##### Modify code Here #####
    ans_list.append(nested_list[0][0]) #nested_list의 첫번째 리스트의 첫 원소를 ans_list에 append
    ans_list.append(nested_list[-1][-1]) #nested_list의 마지막 리스트의 마지막 원소를 ans_list에 append
    ##### End of your code #####
    return ans_list

