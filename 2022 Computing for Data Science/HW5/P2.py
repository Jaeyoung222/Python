def P2(s: str) -> int:
    ### Modify code here ###
    #initialization
    #set integer n and if find character, plus remained length of word.
    word = ""
    n = 0
    for i in range(len(s)) :
        if i+n >= len(s) :
            break
        else :
            if ord(s[i+n])<72 :
                word += s[i+n]
                continue
            elif ord(s[i+n])==122 :
                word += "0"
                n += 3
                continue
            elif ord(s[i+n])==111 :
                word += "1"
                n += 2
                continue
            elif ord(s[i+n])==116 :
                if ord(s[i+n+1])==119 :
                    word += "2"
                    n += 2
                    continue
                else :
                    word += "3"
                    n += 4
                    continue
            elif ord(s[i+n])==102 :
                if ord(s[i+n+1])==111 :
                    word += "4"
                    n += 3
                    continue
                else :
                    word += "5"
                    n += 3
                    continue
            elif ord(s[i+n])==115 :
                if ord(s[i+n+1]) == 105 :
                    word += "6"
                    n += 2
                    continue
                else :
                    word += "7"
                    n += 4
                    continue
            elif ord(s[i+n]) == 101 :
                word += "8"
                n += 4
                continue
            elif ord(s[i+n]) == 110 :
                word += "9"
                n += 3
                continue
    return(int(word))
            
            
    ### End of your code ###