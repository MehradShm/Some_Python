n = int(input())

x = []

for i in range(n):
    x.append([])
for i in x:
    for j in range(n):
        i.append(0)

for i in range(n):
    x[i][i] = 1
for i in range(n):
    x[i][0]=1

for i in range(1 , n):
    for j in range(i+1,n):
        x[j][i] = x[j-1][i-1] + x[j-1][i]

for i in range(n):
    for j in range(i+1):
        print(x[i][j],end=" ")
    print("")
