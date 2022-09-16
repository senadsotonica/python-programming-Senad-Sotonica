import math

a = [3, 5]                                                                      # punkt a
b = [-2, 4]                                                                     # punkt b

dist = math.dist(a, b)                                                          # funktion/metod som beräknar avstånd mellan två punkter
                                                                                # hittade den på w3schools
print("The two points are", a, " and ", b, " .")
print("The distance between the two points is", round(dist, 2), " .")           # matar ut avstånd
