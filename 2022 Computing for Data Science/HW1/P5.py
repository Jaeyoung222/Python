from typing import List
def P5(alphabet_list: List[str]) -> int:
    idx = 0
    ### Modify code here ###
    # list를 string으로 바꾸고 모든 item이 소문자이면 idx에 -1을 assign
    # 아닌 경우, 각 item을 순차적으로 대문자인지 검사함.
    if str(alphabet_list).islower() :
        idx = -1
    else :
        while alphabet_list[idx].islower() :
            idx += 1
    ### End of your code ###  
    return idx
