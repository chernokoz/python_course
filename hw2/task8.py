def primes(number):
    return [i for i in range(2, number + 1)
            if all([(i % j) != 0 for j in range(2, i)])]
