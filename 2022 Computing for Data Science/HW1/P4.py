from typing import List
def P4(word_num_list: List[list]) -> list:
    ans_list = [] 
    ### Modify code here ###
    for n in range(len(word_num_list)) :
        ans_list.append(word_num_list[n][0]) #word_num_list의 각 item list에서 첫번째 item들을 ans_list에 차례로 더함
        ans_list.sort() #오름차순으로 정렬
    ### End of your code ###  
    return ans_list
    