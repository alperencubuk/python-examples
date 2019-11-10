# Prime Factors

N = 120

def primeFactors(number):
    primes = {}
    i = 2
    while number > 1:
        if number % i == 0:
            number /= i
            primes[i] = primes.get(i, 0) + 1
        else:
            i += 1
    return primes

result = ''
for key, value in primeFactors(N).items():
    result += f'{key}^{value} * '
print(result[:-2])

# Alperen Cubuk