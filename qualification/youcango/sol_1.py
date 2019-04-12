t = int(input())
for i in range(1, t + 1):
    n = int(input())
    path = str(input())
    sol = str()
    for k in range(n+n-2):
        if (path[k] == 'S'):
            sol = sol + 'E'
        if (path[k] == 'E'):
            sol = sol + 'S'
    print("Case #{}: {}".format(i, sol))
