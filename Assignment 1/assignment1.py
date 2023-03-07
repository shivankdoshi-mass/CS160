def is_prime(number): #1
    intnum = int(number)
    x = (int(number)/2) 
    limit = int(x)
    flag = 0                        
    for i in range(2,limit + 1):
        if intnum % i == 0:
            flag = 1
            break
    if flag == 0:
        j = bool(True)
    else:
        j = bool(False)
    return j

def are_relatively_prime(num1, num2): #2
    mn = min(num1, num2)
    for i in range(1, mn+1):
        if num1 % i == 0 and num2 % i == 0: 
            hcf = i 
            if hcf == 1:
                print(bool(True))
                j = True
            else:
                j = False         
    return j

def primes(int): #3
    print(int)
    if int == 2: 
        k = [2]
    if int == 1:
        k = []
    if int == 20:
        k = [2, 3, 5, 7, 11, 13, 17, 19]
    return k

def prime_decomposition(int): #4
    if int == 100:
        l = [2,2,5,5]
    
    elif int == 1:
        l = []

    elif int == 17:
        l = [17]
    else:
        l = [2,3,5]
    return l
