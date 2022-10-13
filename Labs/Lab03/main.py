
import sys

sys.path.append(".")

from shapes import Circle
from shapes import Rect




circle = Circle()
print(circle.is_unit_circ())
circle.translate(3,3)
print(circle.is_unit_circ())
print(type(circle))
print(circle.iam())

rect = Rect()
print(rect > circle)
print(rect.area)
print(circle.area)
print(rect.is_sqr())
