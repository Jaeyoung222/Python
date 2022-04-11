from typing import List

def P4(matrix: List[List[int]], target: int) -> (int, int):        
    ##### Write your Code Here #####    
    #do binary search
    #first, find target's row
    start, end = 0, len(matrix)-1
    while start != end + 1 :
        mid = (start + end) // 2
        if matrix[mid][0] < target :
            start = mid + 1
        else :
            end = mid - 1
    #to reduce time, if the first item of founded row is target, return answer
    #for target on (0,0)
    if matrix[start-1][0] == target :
        return (start-1,0)
    #for target on (x,0), x is not 0
    if start < len(matrix) and matrix[start][0] == target :
        return (start,0)
    
    #next, find target's column
    row_start, row_end = 0, len(matrix[start-1])-1
    while row_start != row_end + 1 :
        row_mid = (row_start + row_end) // 2
        if matrix[start-1][row_mid] < target :
            row_start = row_mid + 1
        else :
            row_end = row_mid - 1
    #return the coordinate of target, and if there is not target, return (-1,-1)
    if row_start < len(matrix[start-1]) and matrix[start-1][row_start] == target :
        return (start-1, row_start)
    else :
        return (-1, -1)
    
    ##### End of your code #####