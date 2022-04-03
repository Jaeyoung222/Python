def P7(dct: dict) -> int:
    ### Write code here ###
    #리스트 생성
    l1 = []
    #dct에 있는 모든 value인 dictionary들의 key를 중복 허용하지 않고 l1에 append
    for key in dct :
        if list(dct[key].keys()) not in l1 :
            l1.append(list(dct[key].keys()))
    ans = 1    
    #dct의 각각의 value dictionary에 대하여 key들을 리스트로 생성하고 l1과 같은지 검사 후, 같지 않으면 ans에 0을 assign하고 break
    for key in dct :
        l2 = []
        l2.append(list(dct[key].keys()))
        if l2 != l1 :
            ans = 0
            break
    return ans

    ### End of your code ###     
