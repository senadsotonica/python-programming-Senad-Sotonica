# som uppgift 5 men med x, y, z koordinater
import math

a = [2, 1, 4]                                                                     # punkt a
b = [3, 1, 0]                                                                     # punkt b

dist = math.dist(a, b)                                                            # funktion/metod som beräknar avstånd mellan två punkter
                                                                                  # fungerar i tre dimensioner också :)
print("The two points are", a, " and ", b, " .")
print("The distance between the two points is", round(dist, 2), " .")             # matar ut avstånd
