cimport sys
l1 = input()
l = l1.split()
x=int(l[0])
y=int(l[1])
h=12-x
m=60-y
if h==12:
    print("00",end='')
elif h<10:
    print("0",end='')
    print(h,end='')
else:
    print(h,end='')

if m==60:
    print(":00",end='')
elif m<10:
    print(":0",end='')
    print(m)
else:
    print(":",end='')
    print(m)
