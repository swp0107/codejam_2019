def isFourPresent(x):
    while (x > 0):
        if (x % 10 == 4):
            break
        x = int(x/10)
    return (x > 0)

def whichFourPresent(x):
    i = 0
    while (x > 0):
        if (x % 10 == 4):
            return (i)
        x = int(x/10)
        i = i + 1
    return (False)

t = int(input())
for i in range(1, t+1):
    #n, m = [int(s) for s in input().split(" ")]
    n = int(input())
    #ori = n
    if (isFourPresent(n)):
        m = int(n/2)
        n = n-m
        while (isFourPresent(n) or isFourPresent(m)):
            p = whichFourPresent(n)+1
            #print(n)
            q = whichFourPresent(m)+1
            #print(m)
            #print(p)
            #print(q)
            if (p):
                n = n-pow(10,p-1)
            if (q):
                m = m+pow(10,q-1)
            #print("\n")
            #print(n)
            #print(m)
            #print("\n")

            #if (n+m != ori):
            #    if (n+m < ori):
            #        m = m+1
            #    else:
            #        m = m-1
            #print(n)
            #print(m)
            #print(m+n)
            #print("\n")
        print("Case #{}: {} {}".format(i, n, m))
