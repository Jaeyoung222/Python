from typing import List
def P6(n1: int, n2: int) -> List[int]:
    ans_list = []
    ### Modify code here ###
    a = min(n1, n2) #n1, n2중 최소값을 a에 assign
    #a부터 n1, n2 중 최대값까지 ans_list에 append
    while a <= max(n1, n2) :
        ans_list.append(a)
        ans_list.sort(reverse=True)
        a += 1
    ### End of your code ###
    return ans_list

