def P10(words: set, query_word: str) -> bool:
    ### Write code here ###
    # set은 not subscriptable 하므로 list를 생성
    words_list = list(words)
    ans = False
    for i in range(len(words_list)) : #set 안에 있는 각각의 item에 대하여
        if len(words_list[i]) == len(query_word) : #query_word와 길이가 같은지 확인 하고
            check = 0
            for n in range(len(query_word)) : #길이가 같은 item 중, 각각의 문자에 대하여
                if words_list[i][n] == query_word[n] : #각 index의 문자들이 서로 같은지 확인하고, 같다면 check에 1을 더함.
                    check += 1
            if check == len(query_word) -1 : #check에 더해진 값이 길이에서 1을 뺀 값이라면 문제의 조건을 만족하므로 ans에 True를 assign
                ans = True
            else : #아니라면 check에 0을 다시 assign하고 초기화
                check = 0
        else :
            continue
    return ans
   
    ### End of your code ###     
