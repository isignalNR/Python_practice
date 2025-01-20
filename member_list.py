#checking in list
var = [10,20,30,40]
a = 20
b = 10
c = a-b
d = a/2
print (a, "in", var, ":", a in var)
print (b, "not in", var, ":", b not in var)
print (c, "in", var, ":", c in var)
print (d, "not in", var, ":", d not in var)

print(0x15 in [10, 20, 30, 40])

#checking in tuple
var = (10,20,30,40) #sub tuple dont exit, thats why false
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)
var = ((10,20),30,40) #sub tuple exists, thats why true
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)
