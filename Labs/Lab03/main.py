
import sys

sys.path.append(".")

from shapes import Shape
from shapes import Circle
from shapes import Rect
from shapes import Sphere
from shapes import Cuboid



c1 = Circle()
c2 = Circle(2)

if c1 == c2:
    if c1 < c2:
        print("\n(c1 & c2) == circles, c1 is smaller")
        c1.show()
        c1.translate(3, 4)
        c1.show()

r1 = Rect()
r2 = Rect(2)

if r1 == r2:
    if r1 < r2:
        print("\n(r1 & r2) == rectangles, r1 is smaller")
        r1.show()
        r1.translate(3, 4)
        r1.show()

s1 = Sphere()
s2 = Sphere(2)
print(s1.i_am())
if s1 == s2:
    print("ok")
    if s1 < s2:
        print("\n(s1 & s2) == spheres, s1 is smaller")
        s1.show()
        s1.translate(3, 4, 5)
        s1.show()











