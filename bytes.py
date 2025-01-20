# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)      

# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)

# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])
print(value)

data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)
