from math import gcd

def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d); n //= d
        d += 1
    if n > 1: f.add(n)
    return f

def lcg(seed, a, c, m, n):
    x = seed
    print("i    Xi    Ri")
    print(f"0    {x:<5} {x / m:.4f}")
    for i in range(1, n + 1):
        x = (a * x + c) % m
        print(f"{i:<4} {x:<5} {x / m:.4f}")

def find_period(seed, a, c, m):
    # remember every value seen, so it works even if the seed itself never returns
    seen, x, i = {}, seed, 0
    while x not in seen:
        seen[x] = i
        x = (a * x + c) % m
        i += 1
    return i - seen[x]          # cycle length

def full_period_check(a, c, m):
    if c == 0:
        return None   # Hull-Dobell is for c != 0
    ok1 = gcd(c, m) == 1
    ok2 = all((a - 1) % p == 0 for p in prime_factors(m))
    ok3 = (m % 4 != 0) or ((a - 1) % 4 == 0)
    return ok1, ok2, ok3

seed = int(input("Seed X0 : "))
a = int(input("a       : "))
c = int(input("c       : "))
m = int(input("m       : "))
n = int(input("How many numbers : "))

if m <= 0 or not (0 <= seed < m) or not (0 <= a < m) or not (0 <= c < m):
    print("Need m > 0 and 0 <= X0, a, c < m")
    raise SystemExit

lcg(seed, a, c, m, n)
p = find_period(seed, a, c, m)
print("Period =", p, "(full period)" if p == m else "(not full period)")
chk = full_period_check(a, c, m)
if chk:
    print("Hull-Dobell: gcd(c,m)=1:", chk[0], "| (a-1) divisible by all prime factors of m:", chk[1], "| 4-rule:", chk[2])