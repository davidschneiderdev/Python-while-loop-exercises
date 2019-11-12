
user_int = int(input("Type in a number to receive its factors: "))
prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
        37, 41, 43, 47, 53, 59, 
        61, 67, 71, 73, 79, 83, 
        89, 97, 101, 103, 107, 109, 
        113, 127, 131, 137, 139, 149, 
        151, 157, 163, 167, 173, 179, 
        181, 191, 193, 197, 199]
primes_used = []
remainders = [user_int]

should_restart = True
while should_restart:
    should_restart = False
    for prime in prime_lst:
        if remainders[-1] == 1:
            break
        if remainders[-1] % prime == 0:
            result = remainders[-1] / prime
            remainders.append(result)
            primes_used.append(prime)
            should_restart = True
            break
            
print(primes_used)







