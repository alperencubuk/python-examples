# Sum of the prime numbers under the limit

def sum_of_primes(limit):
    if limit <= 2:
        return 0
    sum = 2
    for i in range(3,limit,2):
        prime = True
        for j in range(2,int(i**0.5)+1):
            if (i % j) == 0:
                prime = False
                break
        if prime:
            sum += i
    return sum

print(sum_of_primes(10))

# Alperen Cubuk