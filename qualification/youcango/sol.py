t = int(input())
for i in range(1, t + 1):
    n = int(input())
    path = str(input())
    matrix = [[0 for x in range(n)] for y in range(n)]
    x = 0
    y = 0
    for i in range(n+n-2):
        if (path[i] == "E"):
            matrix[x][y] = 1
            y = y+1
        if (path[i] == "S"):
            matrix[x][y] = 2
            x = x+1

    sol = str()
    p = 0
    q = 0
    for i in range(n+n-2):
        if (matrix[p][q] == 1):
            sol = sol + "S"
            p = p+1
        if (matrix[p][q] == 2):
            sol = sol + "E"
            q = q+1

    print("Case #{}: {}".format(i, sol))
