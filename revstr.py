def reverse(s):
    if len(s) == 0:
        return s
    else:
        print(s + s[0])
        print(s[0])
        print(s[1:])
        return reverse(s[1:]) + s[0]

s = "iSignalPython"

reverse(s)
