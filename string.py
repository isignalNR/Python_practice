str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

var="HELLO PYTHON"
print ("var:",var)
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])
print(var[-9])
print(var[-4])

var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
   
s = "HelloWorld"
str = ""
for i in s:
    str = i + str
    print(str)

#print(str[0:len(s)])

