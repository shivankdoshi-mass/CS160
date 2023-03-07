import math

def is_prime(n):
    next_number_to_check = 2
    while (next_number_to_check <= math.sqrt(n)):
        if (n%next_number_to_check) == 0:
            return(False)
        next_number_to_check = next_number_to_check + 1
    return(True)

def are_relatively_prime(x, y):
    next_number_to_check = 2
    check_up_to = min(x,y)
    while (next_number_to_check <= check_up_to):
        if (x%next_number_to_check == 0 and y%next_number_to_check == 0):
            return(False)
        next_number_to_check = next_number_to_check +1
    return(True)

def primes(n):
    next_number_to_try = 2
    list_to_return = []
    while (next_number_to_try <= n):
        if (is_prime(next_number_to_try)):
            list_to_return.append(next_number_to_try)
        next_number_to_try = next_number_to_try +1
    return(list_to_return)

def prime_decomposition(n):
    decomposition = []
    whats_left = n
    next_candidate = 2
    while (whats_left > 1):
        if (whats_left%next_candidate == 0 and is_prime(next_candidate)):
            decomposition.append(next_candidate)
            whats_left = whats_left/next_candidate
        else:
            next_candidate = next_candidate + 1
    return(decomposition)
        
