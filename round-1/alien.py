t = int(input())
for i in range(1, t+1):
    n = int(input())
    words = []
    sol = 0
    for j in range(n):
        words.append(str(input()))

    k = 1
    words = sorted(words, key=len, reverse=True)
    lword = words[0]

    r = []
    for q in range(1, len(lword)+1):
        r.append(lword[-q:])
    r.reverse()

    for p in range(1, len(words)):
        for x in range(len(r)):
            if r[x] in words[p]:
                sol += 1
                r.pop(0)

    print("Case #{}: {}".format(i, sol*2))
