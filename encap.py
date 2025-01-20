class Desktop:
   def __init__(self):
      self._max_price = 25000

   def sell(self):
      return f"Selling Price: {self._max_price}"

   def set_max_price(self, price):
      if price > self._max_price:
         self._max_price = price

# Object
desktopObj = Desktop()
print(desktopObj.sell()) 

# modifying the price directly
desktopObj._max_price = 35000
print(desktopObj.sell()) 

# modifying the price using setter function
desktopObj.set_max_price(40000)
print(desktopObj.sell())        

