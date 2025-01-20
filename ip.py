s = "192.168.242.32"
parts = s.split('.')
print(parts)

countvalid=0
countinvalid=0
for i in range(4):
    str = int(parts[i])
    if 0<=str and str<=255:
        countvalid = countvalid+1
        print("Valid number",countvalid)
    else:
        countinvalid = countinvalid+1
        print("invalid number",countinvalid)

if countinvalid ==1:
    print("ip address is invalid")
else:
    print("ip address is valid")
