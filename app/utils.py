from collections import Counter


def is_mersenne(x: int):
    num = x + 1
    count = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            count += 1
        else:
            return False
    return count


def prime_count(number: int) -> str:
    """素因数分解を返す。例: 60 -> '2**2*3*5'"""
    mersenne_num = is_mersenne(number)
    if mersenne_num:
        s = 4
        M = (2**mersenne_num) - 1
        for _ in range(2, mersenne_num):
            s = (s**2 - 2) % M
        if s == 0:
            return f"{number}*1"

    if number < 2:
        return f"{number}*1"
    if number == 2:
        return "2*1"

    primes = []
    while number % 2 == 0:
        primes.append(2)
        number //= 2

    divisor = 3
    while divisor * divisor <= number:
        while number % divisor == 0:
            primes.append(divisor)
            number //= divisor
        divisor += 2

    if number > 1:
        primes.append(number)

    counter = Counter(primes)
    return "*".join(
        f"{p}**{count}" if count > 1 else str(p) for p, count in sorted(counter.items())
    )
