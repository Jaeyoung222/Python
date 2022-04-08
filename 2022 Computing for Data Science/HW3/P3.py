def P3(filename: str) -> list:        
    ##### Write your Code Here #####
    #initialization
    ans = []
    #read line in file
    #    check it starts with '#' or '//'
    #    if not, append line into ans
    with open(filename, 'r') as input_file :
        for line in input_file :
            if line.startswith('#') or line.startswith("//") :
                continue
            else :
                ans.append(line)
    return ans
    ##### End of your code #####