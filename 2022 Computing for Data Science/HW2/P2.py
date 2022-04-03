def P2(lst1: list, lst2: list) -> set:
    ### Write code here ###
    #리스트 l1 생성
    l1 = []
    #lst1과 lst2의 길이가 같으므로 index가 같은 각 item들을 tuple로 묶어서 l1에 append
    for n in range(len(lst1)) :
        l1.append((lst1[n],lst2[n]))
    #l1으로 set을 생성
    s1 = set(l1)
    return s1

    ### End of your code ###     
