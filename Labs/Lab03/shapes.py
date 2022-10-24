from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from math import pi


#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Shape                                                           ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Shape:    
# All shapes are defined by area, circumference and a position                                                  
   def __init__(self, area, circmf, x, y):                        # all shapes have position x,y
      self.x       = x                                            # an area and circumference
      self.y       = y                                             
      self._area   = area                                         # area and circumference are "private"
      self._circmf = circmf                                       # because they can only change if the shape changes

   @property                                                      # getter for area
   def area(self):
      return self._area

   @area.setter                                                   # setter for area           
   def area(self, value):
      self._area = value
         
   @property                                                      # getter for circumference
   def circmf(self):
      return self._circmf

   @circmf.setter                                                 # setter for circumference
   def circmf(self, value):
      self._circmf = value

   def __repr__(self) -> str:                                     # attributes in a string
      return "%s %s %s %s" % (
         self._area, self.circmf, self.x, self.y)

   def __str__(self) -> str:                                      # attributes in a string clearified
      return "area: %s circumference: %s pos: %s, %s\n" % (
         round(self._area, 2), round(self.circmf, 2), self.x, self.y)

   def __eq__(self, other) -> bool:                               # overloading == to be able to compare shapes
      if type(self) == type(other):                               # if shapes are of same type return true
         return True
      else:
         return False

   def __gt__(self, other) -> bool:                               # overloading > to compare area of shapes
      if self._area > other._area:
         return True
      else:
         return False

   def __ge__(self, other) -> bool:                               # overloading >=
      if self._area >= other._area:
         return True
      else:
         return False

   def __lt__(self, other) -> bool:                               # overloading <
      if self._area < other._area:
         return True
      else:
         return False

   def __le__(self, other) -> bool:                               # overloading <= 
      if self._area <= other._area:
         return True
      else:
         return False

   def translate(self, x, y):                                     # move shape to a new position 
      if type(x) == str or type(y) == str:                        # check if x or y are a string
         raise ValueError(                                        # raise ValueError if that is the case
            "Use translate() only with numerical values.") 
      self.x = x
      self.y = y

   def i_am(self):                                                # returns what class the object is
      return type(self)



#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Circle                                                          ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Circle(Shape):                                              # Circle is a shape
   def __init__(self, r = 1, x = 0, y = 0):                       # Circle is by default a unitcircle                                                                      
      self._r     = r                                             # setting circles radius to r                                              
      area        = pi * (r ** 2)                                 # calculating area
      circmf      = 2 * pi * r                                    # and circumference
      Shape.__init__(self, area, circmf, x, y)                    # manifesting the inherited part of shape in circle

   @property
   def r(self):
      return self._r

   @r.setter                                                      # everytime r changes
   def r(self, r):
      self._r      = r
      self._area   = pi * r ** 2                                  # area and
      self._circmf = 2 * pi * r                                   # circumference are recalculated

   def __repr__(self) -> str:                                     # attributes of circle in a string
      return "%s %s %s" % (
         Shape.i_am(self), self._r, Shape.__repr__(self))

   def __str__(self) -> str:                                      # attributes with clarification in a string
      return "\nclass: %s radius: %s %s" % (
         Shape.i_am(self), self._r, Shape.__str__(self))


   def is_unit(self) -> bool:                                     # checks if circle is a unit circle
      if self._r == 1 and self.x == 0 and self.y == 0:
         return True
      else:
         return False
   
   def is_inside(self, x, y) -> bool:                             # using Pythagorean equation to calculate distance 
      if ((x - self.x) * (x - self.x) +                           # from mid in circle to point x,y 
          (y - self.y) * (y - self.y)                             # and compare it to radius
          <= self._r * self._r):
        return True                                               # if radius is equal or greater, point is inside circle
      else:
        return False

   def show(self):                                                # showing circle in x y diagram
      fig, ax  = plt.subplots()                                   # won't work without fig
      lim      = self._r * 2                                      # setting the range of x and y axis to 
      plt.xlim([self.x - lim, self.x + lim])                      # from negative double to double radius
      plt.ylim([self.y - lim, self.y + lim])                      # making sure the whole circle shows
      plt.axis('equal')                                           # setting equal presentation  of axis, so the circle doesn't look oval 
      ax.add_patch(plt.Circle((self.x, self.y ), self._r,         # add circle to plot, set fill to false, making the circle hollow
                   fill = False ))                                
      plt.show()                                                  # display plot



#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Rectangle                                                       ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Rect(Shape):
   def __init__(self, side_a = 1, side_b = 1, x = 0, y = 0):      # by default creating a cube 1x1 at origo
      self._side_a = side_a                                       # setting side_a
      self._side_b = side_b                                       # setting side_b
      area         = side_a * side_b                              # calculating
      circmf       = side_a * 2 + side_b * 2
      Shape.__init__(self, area, circmf, x, y)                    # manifesting the inherited part of shape in rectangle

   @property                                                      # getter side a
   def side_a(self):
      return self._side_a

   @side_a.setter                                                 # setter side a 
   def side_a(self, side_a):                                      # everytime side_a changes recalculate
      self._side_a    = side_a    
      self._area      = self.side_a * self.side_b                 # area and 
      self._circmf    = self.side_a * 2 + self.side_b * 2         # circumference

   @property                                                      # getter side a
   def side_b(self):
      return self._side_b

   @side_b.setter                                                 # setter side b
   def side_b(self, side_b):                                      # everytime side_b changes recalculate
      self._side_b   = side_b
      self._area      = self._side_a * self._side_b               # area and 
      self._circmf    = self._side_a * 2 + self._side_b * 2       # circumference
   
   def __repr__(self) -> str:                                     # attributes as string
      return "%s %s %s %s" % (
         Shape.i_am(self), self._side_a, self._side_b, Shape.__repr__(self))

   def __str__(self) -> str:                                      # attributes as string clearified
      return "\nclass: %s side a: %s side b: %s %s" % (
         Shape.i_am(self), self._side_a, self._side_b, Shape.__str__(self))

   def is_sqr(self) -> bool:                                      # is the rectangle a square
      if self._side_a == self._side_b:
         return True                                              # return true if side a equals side b
      else:
         return False

   def show(self):                                                # showing circle in x y diagram
      fig, ax  = plt.subplots()                                   # won't work without fig
      xlim     = self._side_a * 2
      ylim     = self._side_b * 2                                      
      plt.xlim([self.x - xlim, self.x + xlim])                    # setting the range of x axis
      plt.ylim([self.y - ylim, self.y + ylim])                    # setting the range of y axis
      plt.axis('equal')                                           # setting equal presentation  of axis
      x = self.x - self._side_a / 2                               # adjousting x for plot
      y = self.y - self._side_b / 2                               # adjousting y for plot
      ax.add_patch(plt.Rectangle((x, y ), self.side_a, 
                             self.side_b, fill = False ))         # add rectangle to plot
      plt.show()                                                  # display plot



#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Shape 3d                                                        ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Shape3d(Shape):                                             # inherit shape
   def __init__(self, volume, z):                                 # all 3d shapes have a volume and besides a x,y a z position
      self._volume = volume
      self.z       = z

   def __gt__(self, other) -> bool:                               # overloading > to compare volume of shapes
      if self._volume > other._volume:
         return True
      else:
         return False

   def __ge__(self, other) -> bool:                               # overloading >=
      if self._volume >= other._volume:
         return True
      else:
         return False

   def __lt__(self, other) -> bool:                               # overloading <
      if self._volume < other._volume:
         return True
      else:
         return False

   def __le__(self, other) -> bool:                               # overloading <= 
      if self._volume <= other._volume:
         return True
      else:
         return False

   def translate(self, x, y, z):
      if type(z) == str:                                          # check if z is a string, x and y are checked in Shape.translate()
         raise ValueError(                                        # raise ValueError if that is the case
            "Use translate() only with numerical values.")
      Shape.translate(self, x, y)                                 # translate x and y 
      self.z = z

   def __repr__(self):                                            # attributes as string
      return "%s %s %s %s\n" % (
         self._volume, self.x, self.y, self.z)

   def __str__(self):                                             # attributes as string clearified
      return "volume: %s position: %s, %s, %s\n" % (
         round(self._volume, 2), self.x, self.y, self.z)

   

#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Sphere                                                          ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Sphere(Shape3d, Circle):                                    # a sphere inherits shape3d and circle
   def __init__(self, r = 1, x = 0, y = 0, z = 0):
      volume = (4 / 3) * pi * pow(r, 3)
      Circle.__init__(self, r, x, y)
      Shape3d.__init__(self, volume, z)

   @property
   def r(self):
      return self._r

   @r.setter
   def r(self, r):                                                # changing value of r 
      self._volume = (4 / 3) * pi * pow(r, 3)                     # changes value of volume
      self._r = r

   def __repr__(self) -> str:                                     # attributes as string
      return "%s %s %s" % (
         Shape.i_am(self), self._r, Shape3d.__repr__(self))
   
   def __str__(self) -> str:                                      # attributes as a string clarified
      return "\nclass: %s radius: %s, %s" % (
         Shape.i_am(self), self._r, Shape3d.__str__(self))

   def is_unit(self) -> bool:                                     # is sphere a unit sphere
      if Circle.is_unit(self) and self.z == 0:                    # if (x,y is at origo and r is 1) and z is 0 then true
         return True
      else:
         return False

   def is_inside(self, x, y, z) -> bool:                          # calculating distance from centre of the sphere to the point
      if ((pow((x - self.x), 2) +                                 # if radius is greater than distance, the point is inside the sphere
           pow((y - self.y), 2) + 
           pow((z - self.z), 2)) < pow(self._r, 2)):
         return True
      else:
         return False

   def show(self):                                                # copy paste from
      plt.rcParams["figure.figsize"] = [7.00, 3.50]               # https://www.tutorialspoint.com/plotting-points-on-the-surface-of-a-sphere-in-python-s-matplotlib
      plt.rcParams["figure.autolayout"] = True                    # modified itsy bitsy by me
      fig = plt.figure()
      ax = fig.add_subplot(projection='3d')
      u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
      x = self._r * np.cos(u) * np.sin(v) + self.x
      y = self._r * np.sin(u) * np.sin(v) + self.y
      z = self._r * np.cos(v) + self.z
      ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
      plt.show()


#---- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Cuboid                                                          ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
class Cuboid(Shape3d, Rect):                                      # inherit shape3d and rectangle
   def __init__(self, side_a =1, side_b =1 ,
               side_c =1, x = 0, y = 0, z = 0):
      Rect.__init__(self, side_a, side_b, x, y)                   # manifest rectangle
      self._side_c = side_c
      volume = self._area * side_c
      Shape3d.__init__(self, volume, z)                           # manifest 3rd dimension

   def __repr__(self) -> str:                                     # attributes as string
      return "%s %s %s %s %s %s %s %s %s" % (
                self._side_a, self._side_b, self._side_c,
                 self._volume,
                  self.x, self.y, self.z)

   def __str__(self) -> str:                                      # attributes as a string clarified
      return "\nclass: %s side a: %s side b: %s side c: %s volume: %s pos: %s, %s, %s\n""" % (
         Shape.i_am(self), self._side_a, self._side_b, self._side_c,
                   self._volume, self.x, self.y, self.z)          # this is an alternative to calling Shape3d._str_(self)

   @property
   def side_a(self):
      return self._side_a

   @side_a.setter
   def side_a(self, side_a):
      self._side_a = side_a
      self.adj_volume()

   @property
   def side_b(self):
      return self._side_b

   @side_b.setter
   def side_b(self, side_b):
      self._side_b = side_b
      self.adj_volume()

   @property
   def side_c(self):
      return self._side_c

   @side_c.setter
   def side_c(self, side_c):
      self._side_c = side_c
      self.adj_volume()

   def adj_volume(self):                                          # recalculate volume
      self._volume = self._side_a * self._side_b * self._side_c

   def is_cube(self) -> bool:                                     # is the cuboid a cube
      if self._side_a == self._side_b == self._side_c:
         return True
      else:
         return False
      
   def show(self):                                                # modified from https://www.pythonpool.com/matplotlib-draw-rectangle/
      xlow  = self.x - (self._side_a / 2)                         
      xhigh = self.x + (self._side_a / 2)                         # calculating x y z positions
      ylow  = self.y - (self._side_b / 2)                         # of the 8 corners of the cuboid
      yhigh = self.y + (self._side_b / 2)
      zlow  = self.z - (self._side_c / 2)
      zhigh = self.z + (self._side_c / 2)
      points = np.array([                                         # establishing the coordinates
                  [xlow, ylow, zlow],                             # and they have to be in this order
                  [xhigh, ylow, zlow],                            # or it will not be a cuboid, been there, done that
                  [xhigh, yhigh, zlow],                           # I suspect it has something to do with the
                  [xlow, yhigh, zlow],                            # order of Zs in verts
                  [xlow, ylow, zhigh],
                  [xhigh, ylow, zhigh],
                  [xhigh, yhigh, zhigh],
                  [xlow, yhigh, zhigh]])
      Z = points                                                  # Z is way shorter to type than points :)
      fig = plt.figure()
      ax = fig.add_subplot(111, projection='3d')
      r = [-1,1]
      X, Y = np.meshgrid(r, r)
      ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])
      verts = [[Z[0],Z[1],Z[2],Z[3]],                             # points go in here
               [Z[4],Z[5],Z[6],Z[7]],                             
               [Z[0],Z[1],Z[5],Z[4]],
               [Z[2],Z[3],Z[7],Z[6]],
               [Z[1],Z[2],Z[6],Z[5]],
               [Z[4],Z[7],Z[3],Z[0]]]
      ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.20))
      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_zlabel('Z')
      plt.show()                                                  # show cube                                                   
      
      