def P3(info: list) -> str:        
    ##### Write your Code Here #####    
    #initialization
    ans = ""
    #append birth year
    ans += str(info[1])[-2:]
    #append bitrh month
    if len(str(info[2])) == 1:
        ans += "0"+str(info[2])
    else :
        ans += str(info[2])
    #append birth day
    if len(str(info[3])) == 1:
        ans += "0"+str(info[3])
    else :
        ans += str(info[3])
    #append sex type
    if info[0] == 'MALE' :
        if int(info[1]) >= 1900 and int(info[1]) < 2000 :
            ans += "1"
        elif int(info[1]) < 1900 :
            ans += "9"
        else :
            ans += "3"
    else :
        if int(info[1]) >= 1900 and int(info[1]) < 2000 :
            ans += "2"
        elif int(info[1]) < 1900 :
            ans += "0"
        else :
            ans += "4"
    return ans
        
    ##### End of your code #####