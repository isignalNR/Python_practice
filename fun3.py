def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg = arg + 1
   print ("new object after increment", arg, id(arg))
   arg = arg + 1
   print ("new object after incrementi ram", arg, id(arg))
   return arg

var=10
print ("ID before passing:", id(var))
var=var+1
var1 = testfunction(id(var))
print ("value after function call", var1)
