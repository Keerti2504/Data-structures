import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

arr = [3, 7, 1, 4, 6, 6]

primes = []
non_primes = []

# Separate primes and non-primes
for x in arr:
    if isprime(x):
        primes.append(x)
    else:
        non_primes.append(x)

# Sort to keep smaller values
primes.sort()
non_primes.sort()

# Count how many we can keep
min_count = min(len(primes), len(non_primes))

# Start penalty as total sum
penalty = sum(arr)

# Subtract kept elements
for i in range(min_count):
    penalty -= primes[i]
    penalty -= non_primes[i]

# One extra allowed from larger group
if len(primes) > len(non_primes):
    penalty -= primes[min_count]
elif len(non_primes) > len(primes):
    penalty -= non_primes[min_count]

print(penalty)
