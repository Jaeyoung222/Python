from typing import List
def P1(num_list: List[int]) -> List[int]:
    ### Modify code here ###
    num_list.sort() #리스트 정렬
    num_list.remove(1234) #1234 제거
    num_list.extend([4321,2222]) #4321, 2222 추가
    num_list.insert(1,1111) #2번째 자리에 1111 추가
    ### End of your code ###
    return num_list
