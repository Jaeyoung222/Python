def P2(filename: str) -> list:        
    ##### Write your Code Here #####
    #initialization
    ans = []
    #append each line into ans
    with open(filename, 'r') as input_file :
        for line in input_file :
            ans.append(line)
    #reverse ans
    ans.reverse()
    return ans
    ##### End of your code #####