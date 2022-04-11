def P1(n: int) -> bool:        
    ##### Write your Code Here #####
    #initialization
    prime_factor = []
    #find factors of n and append them to prime_factor
    for i in range(n) :
        if n%(i+1) == 0 :
            prime_factor.append(i+1)
    print(prime_factor)
    #if n can be expressed by multiple of two prime factor, factor of n is three or four 
    if len(prime_factor) == 4 or len(prime_factor) == 3:
        return True
    else :
        return False
    ##### End of your code #####