import string

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    sieve = []
    for p in range(2, n):
        if prime[p]:
            sieve.append(p)
    return (sieve)

t = int(input())
for i in range(1, t+1):
    n, m = [int(s) for s in input().split(" ")]
    x = list(map(int, input().split()))
    prime_dict = sieve(n)
    letters = []
    for a in range(len(prime_dict)):
        if (x[0] % prime_dict[a] == 0):
            letters.append(prime_dict[a])
            letters.append(x[0]//prime_dict[a])
            break
    for b in range(1,m):
        letters.append(x[b]//letters[b])

    original = letters
    letters = sorted(letters)
#remove duplicate
#print(original)
#print(letters)
    li = list(dict.fromkeys(letters))
#print(li)
    up = string.ascii_uppercase
    d = dict(zip(li, up))
    sol_d = [d[k] for k in original]
    sol = str()
    for c in sol_d:
        sol = sol + c

    print("Case #{}: {}".format(i, sol))

#print(len(sol))
#print(x[0])
#print(prime_dict)
#print(letters)
#print(len(letters))
