def factorialTrailingZeros(n):
    factProduct = 1
    
    i = 1
    while i <= n:
        factProduct *= i 
        i += 1
     
    leadingZeros = 0
    factProductStr = str(factProduct)
    
    j = len(factProductStr) - 1
    while j > 0:
        if factProductStr[j] == "0":
            leadingZeros += 1
        else:
            break;
        j -= 1
        
    return leadingZeros
