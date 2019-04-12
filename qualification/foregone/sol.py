def isFourPresent(x):
    while (x > 0):
        if (x % 10 == 4):
            break
        x = int(x / 10)
    return (x > 0)

t = int(input())
for i in range(1, t+1):
    #n, m = [int(s) for s in input().split(" ")]
    n = int(input())
    if (isFourPresent(n)):
        m = 1
        n = n-1
        t=0
        while (isFourPresent(n) or isFourPresent(m)):
            n=n-1
            m=m+1
            t=t+1
        print("Case #{}: {} {} {}".format(i, n, m, t))
