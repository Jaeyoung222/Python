def P1(lst: list) -> set:
    ### Write code here ###
    #list와 set을 생성
    l1 = []
    s1 = set()
    #l1에 lst의 item들을 중복 없이 넣고, 중복되면 s1에 add
    for i in lst :
        if i not in l1 :
            l1.append(i)
        else :
            s1.add(i)
    return s1

    ### End of your code ###     
