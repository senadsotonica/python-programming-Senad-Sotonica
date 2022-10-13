
from math import pi

class Shape:    
# All shapes are defined by area, circumference and a position                                                  
   def __init__(self, area, circmf, x, y):
      print("initiating shape")                                            # all shapes have
      self.x      = x                                             
      self.y      = y                                             
      self.area   = area
      self.circmf = circmf

   def __eq__(self, other) -> bool:
   # overloading == to be able to compare shapes
   # if shapes are of same type return true
      if type(self) == type(other):
         return True
      else:
         return False

   def __gt__(self, other) -> bool:
   # overloading > to compare area of shapes
      if self.area > other.area:
         return True
      else:
         return False

   def __ge__(self, other) -> bool:
   # overloading >=
      if self.area >= other.area:
         return True
      else:
         return False

   def __lt__(self, other) -> bool:
   # overloading <
      if self.area < other.area:
         return True
      else:
         return False

   def __le__(self, other) -> bool:
    # overloading <=
      if self.area <= other.area:
         return True
      else:
         return False

   def translate(self, x, y):
   # move to a new position
      self.x = x
      self.y = y

   def iam(self):
      return type(self)




class Circle(Shape):
   def __init__(self, r = 1, x = 0, y = 0):
   # initiate a unit circle by default
      print("circle")
      self.r = r
      area        = pi * r ** 2
      circmf      = 2 * pi * r
      Shape.__init__(self, area, circmf, x, y)
      print(self.r, self.area, self.circmf)

   def is_unit_circ(self) -> bool:
   # checks if circle is a unit circle
      if self.r == 1 and self.x == 0 and self.y == 0:
         return True
      else:
         return False
   
   def is_inside(self, x, y) -> bool:
   # using Pythagorean equation to calculate distance 
   # (from mid in circle to point x,y) 
   # and compare it to radius
      if ((x - self.x) * (x - self.x) +                     
          (y - self.y) * (y - self.y) 
          <= self.r * self.r):
        return True
      else:
        return False




class Rect(Shape):
   def __init__(self, sideA = 1, sideB = 1, x = 0, y = 0):
      print("rectangle")
      self.sideA = sideA
      self.sideB = sideB
      area = sideA * sideB
      circmf = sideA * 2 + sideB * 2
      Shape.__init__(self, area, circmf, x, y)
   
   def is_sqr(self) -> bool:
      if self.sideA == self.sideB:
         return True
      else:
         return False







class Shape_3d(Shape):
   pass

class Sphere(Shape_3d):
   pass

class Cube(Shape_3d):
   pass