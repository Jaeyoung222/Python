def P5(filename: str) -> int:        
    ##### Write your Code Here #####
    #initialization
    ans = 0
    with open(filename, 'r') as input_file :
        for line in input_file :
            #remove whitespace and split by space
            for i in input_file.readline().strip().split() :
                #take length of each word and compare with last maximum value 
                num = len(i)
                if num > ans :
                    ans = num
    return ans
    ##### End of your code #####