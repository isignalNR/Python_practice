import sys

try:
   # open file stream
   file_name = "sample.txt"
   file = open(file_name, "w")
except IOError:
   print ("There was an error writing to", file_name)
   sys.exit()
print ("Enter '", file_name)
print ("' When finished")
while file_text != file_name:
   file_text = raw_input("Enter text: ")
   if file_text == file_name:
      # close the file
      file.close
      break
   file.write(file_text)
   file.write("\n")
file.close()
file_name = raw_input("Enter filename: ")
if len(file_name) == 0:
   print ("Next time please enter something")
   sys.exit()
try:
   file = open(file_name, "r")
except IOError:
   print ("There was an error reading file")
   sys.exit()
file_text = file.read()
file.close()
print (file_text)
