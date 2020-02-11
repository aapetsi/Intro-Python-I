def is_prime(n):
    for x in range(2,n):
        if n % x == 0:
            return False
        return True


print(is_prime(8))


def sieve_of_erasthones(n):
    nums = [x for x in range(2, n+1)]
    primes = []
    x = 2
    while (x < n):
        for idx, i in enumerate(nums):
            if i % x == 0 and i >= x**2:
                nums[idx] = False
        x += 1
    
    for num in nums:
        if type(num) == int:
            primes.append(num)
    return primes

print(sieve_of_erasthones(50))
