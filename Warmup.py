inp = input("Enter Rows And Columns\n")

tmp = inp.split(" ")

rows = int(tmp[0])

columns = int(tmp[1])

#print(rows , columns)

lst = [ [ 0 for j in range(columns) ] for i in range(rows)]

print(lst)
