def P1(filename: str) -> list:        
    ##### Write your Code Here #####
    #initialization
    ans = []
    #make each lines into list, splited by whitespace, and append it at ans. 
    with open(filename, "r") as input_file :
        for line in input_file :
            ans.append(line.split())
    return ans
    ##### End of your code #####