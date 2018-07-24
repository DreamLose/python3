class Triangle:

 
   def __init__(self, bottom, height):
      self.bottom = bottom
      self.height = height

   
   def triangleArea(self):
    	return (self.bottom * self.height /2)

emp1 = Triangle(100, 2000)

result =  emp1.triangleArea()
print result
