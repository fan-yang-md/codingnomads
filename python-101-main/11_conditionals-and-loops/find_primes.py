def find_primes(N):
    primes = [1, 2]
    for N in range(3, N):
        num_factors = 0
        for index, prime in enumerate(primes[1:]):
            # factor found
            if (N % prime == 0):
                num_factors += 1
                continue
            # we went through all primes and found no factor
           # if (index == len(primes) - 1):
        if num_factors == 0:
            primes.append(N)
    return primes, len(primes)

print(find_primes(1001))
