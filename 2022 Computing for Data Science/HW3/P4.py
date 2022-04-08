def P4(filename: str) -> list: 
    ##### Write your Code Here #####
    #initialization
    ans = []
    #read line in file
    #    check it starts with '#' or '//'
    #    if not, replace '#' ans '//' to '*',
    #    and split by '*' and take first one
    #    and remove whitespace and append line into ans
    with open(filename, 'r') as input_file :
        for line in input_file :
            if line.startswith('#') or line.startswith("//") :
                continue
            else :
                ans.append(line.replace('#','*').replace('//','*').split('*')[0].strip())
    return ans
    ##### End of your code #####
    ##### End of your code #####