import random


def check1(n, k, m):
    total = k_count = m_count = 0
    while n >= k:
        k_count = n // k
        m_count = k // m * k_count
        total += m_count
        n -= m_count * m
    return total


def check2(n, k, m):
    i = k - k % m
    n = n - k
    return (n // i + 1) * (k // m)


for _ in range(2000):
    n = random.randint(50, 100)
    k = random.randint(10, n)
    m = random.randint(1, k)
    assert check1(n, k, m) == check2(n, k, m)