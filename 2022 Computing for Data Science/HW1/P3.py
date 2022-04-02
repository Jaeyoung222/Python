from typing import List
def P3(num_list: List[int]) -> List[int]:
    ans_list = [] #새로운 리스트 생성
    ### Modify code here ###
    for n in range(len(num_list)) :
        ans_list.append(-num_list[n]) #각 item에 -1을 곱해서 ans_list에 순서대로 추가
    ### End of your code ###   
    return ans_list
    